'''main page models'''
import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.contrib import admin
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class GeneralSettings(models.Model):
	'''General Website Settings'''
	SLATE = 1
	GRAY = 2
	ZINC = 3
	NEUTRAL = 4
	STONE = 5
	BROWN = 6
	RED = 7
	ORANGE = 8
	AMBER = 9
	YELLOW = 10
	LIME = 11
	GREEN = 12
	EMERALD = 13
	TEAL = 14
	CYAN = 15
	SKY = 16
	BLUE = 17
	INDIGO = 18
	VIOLET = 19
	PURPLE = 20
	FUCHSIA = 21
	PINK = 22
	ROSE = 23
	COLOR_CHOICES = [
		(SLATE, 'Slate'),
		(GRAY, 'Gray'),
		(ZINC, 'Zinc'),
		(NEUTRAL, 'Neutral'),
		(STONE, 'Stone'),
		(BROWN, 'Brown'),
		(RED, 'Red'),
		(ORANGE, 'Orange'),
		(AMBER, 'Amber'),
		(YELLOW, 'Yellow'),
		(LIME, 'Lime'),
		(GREEN, 'Green'),
		(EMERALD, 'Emerald'),
		(TEAL, 'Teal'),
		(CYAN, 'Cyan'),
		(SKY, 'Sky'),
		(BLUE, 'Blue'),
		(INDIGO, 'Indigo'),
		(VIOLET, 'Violet'),
		(PURPLE, 'Purple'),
		(FUCHSIA, 'Fuchsia'),
		(PINK, 'Pink'),
		(ROSE, 'Rose'),
	]

	ward_name = models.CharField(max_length=128, help_text="Required. It will display at the top of the main page.")
	theme_color = models.PositiveSmallIntegerField(default=BROWN, choices=COLOR_CHOICES, help_text="Website Theme Color")
	logo_path = models.FilePathField(
		path=str(settings.STATIC_ROOT / 'main' / 'images'),
		blank=True,
		recursive=True,
		help_text='''Path to the logo displayed in the top-left corner of the webpage.
		If not provided, the corner will be left blank.''')
	photos_path = models.FilePathField(
		path=str(settings.STATIC_ROOT / 'main' / 'images'),
		blank=True,
		allow_folders=True,
		recursive=True,
		help_text='''Path to the directory containing the photos that will be displayed
		randomly on the homepage. If not provided, the quote will be lonely.''')


	def __str__(self):
		return "General Settings"

	class Meta:
		'''Meta class'''
		verbose_name = 'General Settings'
		verbose_name_plural = 'General Settings'


class MeetingTime(models.Model):
	'''Manages meeting date and time'''
	next_meeting_date = models.DateField(
		null=True,
		blank=True,
		help_text='''Optional. The website automatically displays the next Sunday for the meeting date.
			Set a value here to override the next meeting date.'''
	)
	first_hour_meeting_time = models.CharField(max_length=8, help_text='Required. Your Sacrament Meeting meeting time.')
	second_hour_meeting_time = models.CharField(max_length=8, help_text='Required. Your classes meeting time.')

	def get_next_meeting_date(self):
		'''Returns the next sunday, or next_meeting_date if
		it is set and after next_sunday'''
		current_day = datetime.datetime.now(datetime.timezone.utc)
		next_sunday = current_day + datetime.timedelta(days=6-current_day.weekday())

		if self.next_meeting_date is None:
			return next_sunday.strftime('%B %d, %Y')

		if self.next_meeting_date < next_sunday:
			return next_sunday.strftime('%B %d, %Y')

		return self.next_meeting_date.strftime('%B %d, %Y')


	def __str__(self):
		return "Meeting Times"


	class Meta:
		'''Meta class'''
		verbose_name = 'Meeting Times'
		verbose_name_plural = 'Meeting Times'


class BulletinGroup(models.Model):
	'''A group of bulletin entries'''
	enabled = models.BooleanField(
		default=False,
		help_text="Determines if the group should be displayed or not. Only the first enabled group will be displayed."
	)
	name = models.CharField(max_length=255, help_text="The name of the bulletin group. It is only to help you keep track of what entries the group contains, so choose anything you like.")

	def __str__(self):
		return (
			f'{self.name}, enabled: {self.enabled}, entry count: {self.num_entries()}'
		)

	@admin.display(description='Number of Bulletin Entries')
	def num_entries(self):
		'''Returns the number of bulletin entries in the group'''
		return self.bulletinEntries.all().count()  # type: ignore

	class Meta:
		'''Meta class'''
		verbose_name = 'Bulletin Group'
		verbose_name_plural = 'Bulletin Groups'


class BulletinEntry(models.Model):
	'''Rows of the bulletin'''
	SACRAMENT_MEETING = 1
	SUNDAY_SCHOOL = 2
	RELIEF_SOCIETY_AND_PRIESTHOOD = 3
	SECTION_CHOICES = [
		(SACRAMENT_MEETING, 'Sacrament Meeting'),
		(SUNDAY_SCHOOL, 'Sunday School'),
		(RELIEF_SOCIETY_AND_PRIESTHOOD, 'Relief Society and Priesthood')
	]

	bulletin_group = models.ForeignKey(
		BulletinGroup,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='bulletinEntries',
		help_text='Optional. Select which Bulletin Group this entry belongs to.'
	)
	enabled = models.BooleanField(default=True, help_text="Determines if the row should be displayed on the page.")
	section = models.PositiveSmallIntegerField(
		default=SACRAMENT_MEETING,
		choices=SECTION_CHOICES,
		help_text="Required. The page section to appear in."
	)
	position = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		help_text="The order the entry appears within the group. Leave blank to auto-fill with next value."
	)
	title = models.CharField(
		max_length=128,
		help_text="Required. Without a value, will center on the page. With a value included, will be left-justified."
	)
	value = models.CharField(
		max_length=128,
		default='',
		blank=True,
		help_text="Optional. If added, will right-justify in-line with the (now left-justified) title."
	)
	url = models.CharField(max_length=255, null=True, blank=True, help_text="Optional. If added, will add a hyperlink to the Value field.", verbose_name="URL")
	additional_note = models.CharField(
		max_length=128,
		default='',
		blank=True,
		help_text="Optional. If included, will show up to the right of the Value field, outside the hyperlink (for example, the hymn number next to the hymn name)."
	)

	def __str__(self):
		return f'{self.title}{": " if self.value else ""}{self.value}'

	def table_view(self):
		longest = 0
		for field in self._meta.get_fields():  # type: ignore
			longest = max(longest, len(str(getattr(self, field.name))))

		return (
			f'\n{"-" * (longest + 22)}\n' + 
			f'|         Enabled | {self.enabled:<{longest}} |\n' +
			f'|         Section | {self.section:<{longest}} |\n' +
			f'|        Position | {self.position:<{longest}} |\n' +
			f'|           Title | {self.title:<{longest}} |\n' +
			f'|           Value | {self.value:<{longest}} |\n' +
			f'|             URL | {self.url:<{longest}} |\n' +
			f'| Additional Note | {self.additional_note:<{longest}} |\n' +
			f'{"-" * (longest + 22)}\n'
		)

	class Meta:
		'''Meta class'''
		verbose_name = 'Bulletin Entry'
		verbose_name_plural = 'All Bulletin Entries'


@receiver(pre_save, sender=BulletinEntry)
def bulletin_entry_pre_save(sender, instance, **kwargs):
	'''Sets bulletin entry position if it is not set'''
	if instance.position is None:
		instance.position = BulletinEntry.objects.all().count()


class ActiveBulletinEntryManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(bulletin_group__enabled=True)


class ActiveBulletinEntry(BulletinEntry):
	objects = ActiveBulletinEntryManager()
	class Meta:
		proxy = True
		verbose_name = 'Active Bulletin Entry'
		verbose_name_plural = 'Active Bulletin Entries'


class Quote(models.Model):
	enabled = models.BooleanField(
		default=True,
		help_text="Determines if the quote should be added to the display rotation."
	)
	source = models.CharField(max_length=128, help_text="Required. The source of the quote.")
	quote = models.TextField(help_text="Required. The quote content.")
	url = models.CharField(max_length=255, default='', blank=True, help_text="Optional. The optional URL of the quote. If included, will add a hyperlink to the source field under the quote on the homepage.")

	def __str__(self):
		if len(self.quote) > 32:
			return f'{self.source} - {self.quote[0:31]}...'
		return f'{self.source} - {self.quote}'

	class Meta:
		'''Meta class'''
		verbose_name = 'Quote'
		verbose_name_plural = 'Quotes'


class Announcement(models.Model):
	enabled = models.BooleanField(
		default=True,
		help_text="Determines if the announcement should be displayed on the announcements page."
	)
	position = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		help_text="The order the announcement appears on the page. Leave blank to auto-fill with next value."
	)
	content = models.TextField(help_text="Required. Supports markdown formatting")
	name = models.CharField(max_length=128, help_text="Required. Helps you organize your announcments internally.")

	class Meta:
		'''Meta class'''
		verbose_name = 'Announcement'
		verbose_name_plural = 'Announcements'


@receiver(pre_save, sender=Announcement)
def announcement_pre_save(sender, instance, **kwargs):
	'''Sets bulletin entry position if it is not set'''
	if instance.position is None:
		instance.position = Announcement.objects.all().count()


class ContactTable(models.Model):
	'''A group of contacts'''
	enabled = models.BooleanField(
		default=True,
		help_text="Determines if the group should be displayed or not."
	)
	name = models.CharField(
		max_length=255,
		help_text="Required. The name of the contact group. It will appear above the table on the webpage."
	)
	additional_notes = models.TextField(
		blank=True,
		help_text="Optional. Additional notes that will appear below the table on the webpage if set."
	)
	position = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		help_text="The order the table appears on the page. Leave blank to auto-fill with next value."
	)
	raw_content = models.TextField(
		blank=True,
		help_text='''Optional. Adding content here will override the default table layout. Supports
		Markdown and HTML.'''
	)

	def __str__(self):
		if self.raw_content != '':
			if len(self.raw_content) > 128:
				return f'{self.raw_content[0:127]}...'
			return self.raw_content
		return (
			f'{self.name}, enabled: {self.enabled}, entry count: {self.num_entries()}, position: {self.position}'
		)

	@admin.display(description='Number of Contacts')
	def num_entries(self):
		'''Returns the number of contacts in the group'''
		return self.contacts.all().count()  # type: ignore

	class Meta:
		'''Meta class'''
		verbose_name = 'Contact Table'
		verbose_name_plural = 'Contact Tables'


@receiver(pre_save, sender=ContactTable)
def contact_table_pre_save(sender, instance, **kwargs):
	'''Sets contact table position if it is not set'''
	if instance.position is None:
		instance.position = ContactTable.objects.all().count()


class Contact(models.Model):
	name = models.CharField(max_length=128, help_text="Required. The contact's name.")
	email = models.EmailField(blank=True, help_text="Optional. The contact's email address.")
	phone = models.CharField(max_length=20, blank=True, help_text="Optional. The contact's phone number.")
	calling = models.CharField(max_length=128, help_text="Required. The contact's calling.")
	position = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		help_text="The position of the contact in the table on the page. Leave blank to auto-fill with next value."
	)
	contact_table = models.ForeignKey(
		ContactTable,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='contacts',
		help_text='Optional. Select which Contact Table this contact belongs to.'
	)

	def __str__(self):
		return f'{self.name} - {self.calling}'

	class Meta:
		'''Meta class'''
		verbose_name = 'Contact'
		verbose_name_plural = 'All Contacts'


@receiver(pre_save, sender=Contact)
def contact_pre_save(sender, instance, **kwargs):
	'''Sets contact position if it is not set'''
	if instance.position is None:
		instance.position = Contact.objects.all().count()
