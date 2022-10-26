'''main page models'''
import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.contrib import admin
from django.dispatch import receiver

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

	theme_color = models.PositiveSmallIntegerField(default=BROWN, choices=COLOR_CHOICES, help_text="Website Theme Color")

	def __str__(self):
		return self.get_theme_color_display()

	class Meta:
		'''Meta class'''
		verbose_name = 'General Settings'
		verbose_name_plural = 'General Settings'

class MeetingTime(models.Model):
	'''Manages meeting date and time'''
	next_meeting_date = models.DateField(
		null=True,
		blank=True,
		help_text=(
			"The website automatically displays the next Sunday for the meeting date."
			"Set a value here to override the next meeting date."
		)
	)
	first_hour_meeting_time = models.CharField(max_length=8)
	second_hour_meeting_time = models.CharField(max_length=8)

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
		return (
			f'Next Meeting Date: {self.next_meeting_date}, ' +
			f'First Hour: {self.first_hour_meeting_time}, ' +
			f'Second Hour: {self.second_hour_meeting_time}'
		)


	class Meta:
		'''Meta class'''
		verbose_name = 'Meeting Times'
		verbose_name_plural = 'Meeting Times'



class BulletinGroup(models.Model):
	'''A group of bulletin entries'''
	enabled = models.BooleanField(
		default=False,
		help_text="If the group should be displayed or not. Only the first enabled group will be displayed."
	)
	name = models.CharField(max_length=255, help_text="The name of the bulletin entry group")

	def __str__(self):
		return (
			f'{self.name}, enabled: {self.enabled}, entry count: {self.num_entries()}'
		)

	@admin.display(description='Number of Bulletin Entries')
	def num_entries(self):
		'''Returns the number of bulletin entries in the group'''
		return self.bulletinEntries.all().count()

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
		related_name='bulletinEntries'
	)
	enabled = models.BooleanField(default=True, help_text="If the row should be displayed or not.")
	section = models.PositiveSmallIntegerField(
		default=SACRAMENT_MEETING,
		choices=SECTION_CHOICES,
		help_text="The page section to add to."
	)
	position = models.PositiveSmallIntegerField(
		null=True,
		blank=True,
		help_text="The sorting position on the page within the group. Leave blank to auto-fill with next value."
	)
	title = models.CharField(
		max_length=128,
		help_text="Without a value, will center on the page. With a value included, will be left-justified."
	)
	value = models.CharField(
		max_length=128,
		null=True,
		blank=True,
		help_text="If added, will right-justify in-line with the (now left-justified) title."
	)
	url = models.CharField(max_length=255, null=True, blank=True, help_text="If added, will hyperlink the value.")
	additional_note = models.CharField(
		max_length=128,
		null=True,
		blank=True,
		help_text="If included, will show up next to the value (for example, the hymn number)."
	)

	def __str__(self):
		# longest = 0
		# for field in self._meta.get_fields():
		# 	longest = max(longest, len(str(getattr(self, field.name))))

		# return (
		# 	f'\n{"-" * (longest + 22)}\n' + 
		# 	f'|         Enabled | {self.enabled:<{longest}} |\n' +
		# 	f'|         Section | {self.section:<{longest}} |\n' +
		# 	f'|        Position | {self.position:<{longest}} |\n' +
		# 	f'|           Title | {self.title:<{longest}} |\n' +
		# 	f'|           Value | {self.value:<{longest}} |\n' +
		# 	f'|             URL | {self.url:<{longest}} |\n' +
		# 	f'| Additional Note | {self.additional_note:<{longest}} |\n' +
		# 	f'{"-" * (longest + 22)}\n'
		# )
		return f'{self.title}{": " if self.value else ""}{self.value}'

	class Meta:
		'''Meta class'''
		verbose_name = 'Bulletin Entry'
		verbose_name_plural = 'Bulletin Entries'

@receiver(pre_save, sender=BulletinEntry)
def bulletin_entry_pre_save(_, instance, **kwargs):
	'''Sets bulletin entry position if it is not set'''
	if instance.position is None:
		instance.position = BulletinEntry.objects.all().count()
