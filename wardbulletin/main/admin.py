'''Main site admin interfaces'''
from django.contrib import admin
from admin_ordering.admin import OrderableAdmin
from .models import GeneralSettings, MeetingTime, BulletinEntry, ActiveBulletinEntry, BulletinGroup, Quote, Announcement, Contact, ContactTable
from .singleton_admin import DjangoSingletonModelAdmin
from .actions import make_enabled, make_disabled, make_inverted, change_bulletin_group

# Register your models here.

class GeneralSettingsAdmin(DjangoSingletonModelAdmin):
	'''General Settings Admin Interface'''
	fields = [
		'theme_color',
		'logo_path',
		'photos_path',
	]
	list_display = (
		'theme_color',
		'logo_path',
		'photos_path',
	)


class MeetingTimeAdmin(DjangoSingletonModelAdmin):
	'''Meeting Time Admin Interface'''
	fields = [
		'first_hour_meeting_time',
		'second_hour_meeting_time',
		'next_meeting_date',
	]
	list_display = (
		'first_hour_meeting_time',
		'second_hour_meeting_time',
		'next_meeting_date',
	)


class BulletinEntryAdmin(OrderableAdmin, admin.ModelAdmin):
	'''Bulletin Entry Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': '''All of the bulletin entries are contained can be edited
			directly through this interface, if needed. It is easier to edit the bulletin
			entries within a bulletin group directly, but this will allow you to manage
			the entries as needed.'''
		}),
		(None, {
			'fields': (
				'position',
				'title',
				'value',
				'url',
				'additional_note',
				'enabled',
				'section',
				'bulletin_group',
			)
		})
	)
	list_display = (
		'position',
		'title',
		'value',
		'url',
		'additional_note',
		'enabled',
		'section',
		'bulletin_group',
	)
	list_display_links = ('title',)
	list_editable = (
		'position',
		'value',
		'url',
		'additional_note',
		'enabled',
		'section',
		'bulletin_group',
	)
	ordering_field = 'position'
	ordering = ['position']
	actions = [make_enabled, make_disabled, make_inverted, change_bulletin_group]


class BulletinEntryInline(OrderableAdmin, admin.TabularInline):
	'''Bulletin Entry Inline Admin Interface'''
	model = BulletinEntry
	ordering_field = 'position'
	extra = 0
	fields = (
		'position',
		'section',
		'title',
		'value',
		'url',
		'additional_note',
		'enabled',
		'bulletin_group',
	)


class BulletinGroupAdmin(admin.ModelAdmin):
	'''Bulletin Group Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': '''The main bulletin editor. Manage all the associated bulletin entries: 
			add new, modify, or reorder entries associated with this group from here. Use the <i>Save As</i>
			Button at the bottom to duplicate an existing group, along with all of its associated entries.
			Make sure to modify the group after duplicating it!'''
		}),
		(None, {
			'fields': (
				'name',
				'enabled',
			)
		})
	)
	inlines = [BulletinEntryInline]
	list_display = (
		'name',
		'num_entries',
		'enabled',
	)
	list_editable = ('enabled',)
	actions = [make_enabled, make_disabled, make_inverted]
	save_as = True


class QuoteAdmin(admin.ModelAdmin):
	'''Quote Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': 'Each time somebody loads the homepage, a random quote from this table will be chosen and displayed at the top of the page.'
		}),
		(None, {
			'fields': (
				'enabled',
				'source',
				'quote',
				'url',
			)
		})
	)
	list_display = (
		'source',
		'quote_custom_rendering',
		'url',
		'enabled',
	)
	list_editable = ('enabled',)
	actions = [make_enabled, make_disabled, make_inverted]

	@admin.display(description="Quote")
	def quote_custom_rendering(self, obj):
		if len(obj.quote) > 128:
			return f'{obj.quote[0:127]}...'
		return obj.quote


class AnnouncementAdmin(OrderableAdmin, admin.ModelAdmin):
	'''Announcement Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': '''Announcement content can be formatted easily with online editors 
				in either <a href="https://markdown-editor.github.io/" target="_blank">Markdown</a> 
				or <a href="https://html-online.github.io/" target="_blank">HTML</a>. Just copy the 
				markdown or the HTML <b>source code</b> into the content box below. In the  example 
				editor mentioned, the source code is viewable under the <i>View</i> menu.'''
		}),
		(None, {
			'fields': (
				'enabled',
				'position',
				'name',
				'content',
			),
		}),
	)
	list_display = (
		'position',
		'name',
		'content_custom_rendering',
		'enabled',
	)
	list_display_links = ('name',)
	list_editable = (
		'position',
		'enabled',
	)
	ordering_field = 'position'
	ordering = ['position']
	actions = [make_enabled, make_disabled, make_inverted]

	@admin.display(description="Announcement")
	def content_custom_rendering(self, obj):
		if len(obj.content) > 256:
			return f'{obj.content[0:255]}...'
		return f'{obj.content}'


class ContactsInline(OrderableAdmin, admin.TabularInline):
	model = Contact
	ordering_field = 'position'
	extra = 0
	fields = (
		'position',
		'name',
		'calling',
		'email',
		'phone',
	)


class ContactAdmin(OrderableAdmin, admin.ModelAdmin):
	'''Contact Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': '''Manage the contact information for a single contact.'''
		}),
		(None, {
			'fields': (
				'position',
				'name',
				'calling',
				'email',
				'phone',
			)
		})
	)
	list_display = (
		'position',
		'name',
		'calling',
		'email',
		'phone',
	)
	list_editable = (
		'position',
		'calling',
		'email',
		'phone',
	)
	list_display_links = ('name',)
	ordering_field = 'position'
	ordering = ['position']


class ContactTableAdmin(OrderableAdmin, admin.ModelAdmin):
	'''Contact Table Admin Interface'''
	fieldsets = (
		(None, {
			'fields': (),
			'description': '''The main contact table editor. Manage all the associated contacts: 
			add new, modify, or reorder entries associated with this group from here. Use the <i>Save As</i>
			Button at the bottom to duplicate an existing group, along with all of its associated entries.
			Make sure to modify the group after duplicating it! The tables will be displayed in the order
			specified.'''
		}),
		(None, {
			'fields': (),
			'description': '''If the default table layout doesn't work for what you need to display, you can use
		the raw_content field to have full control over what gets displayed. You can put markdown or HTML into
		the raw_content and it will be displayed directly. Any Contacts associated with the table will be ignored,
		so you will need to add them manually to the raw_content as well. 
		[Learn more about markdown tables.](https://www.markdownguide.org/extended-syntax/#tables)'''
		}),
		(None, {
			'fields': (
				'enabled',
				'name',
				'position',
				'additional_notes',
				'raw_content',
			)
		})
	)
	inlines = [ContactsInline]
	list_display = (
		'name',
		'position',
		'num_entries',
		'additional_notes',
		'content_custom_rendering',
		'enabled',
	)
	list_editable = ('position', 'enabled')
	actions = [make_enabled, make_disabled, make_inverted]
	save_as = True
	ordering_field = 'position'
	ordering = ['position']

	@admin.display(description="Raw Content")
	def content_custom_rendering(self, obj):
		if len(obj.raw_content) > 128:
			return f'{obj.raw_content[0:127]}...'
		return f'{obj.raw_content}'


admin.site.register(GeneralSettings, GeneralSettingsAdmin)
admin.site.register(MeetingTime, MeetingTimeAdmin)
admin.site.register(BulletinGroup, BulletinGroupAdmin)
admin.site.register(BulletinEntry, BulletinEntryAdmin)
admin.site.register(ActiveBulletinEntry, BulletinEntryAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactTable, ContactTableAdmin)
