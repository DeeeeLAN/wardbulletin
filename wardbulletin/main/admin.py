'''Main site admin interfaces'''
from django.contrib import admin
from django.db.models import Q
from .models import GeneralSettings, MeetingTime, BulletinEntry, BulletinGroup
from .singleton_admin import DjangoSingletonModelAdmin

# Register your models here.

@admin.action(description="Mark selected rows as Enabled")
def make_enabled(modeladmin, request, queryset):
	queryset.update(enabled=True)

@admin.action(description="Mark selected rows as Disabled")
def make_disabled(modeladmin, request, queryset):
	queryset.update(enabled=False)

@admin.action(description="Invert Enabled/Disabled state for selected rows")
def make_inverted(modeladmin, request, queryset):
	queryset.update(enabled=Q(enabled=False))


class GeneralSettingsAdmin(DjangoSingletonModelAdmin):
	'''General Settings Admin Interface'''
	fields = [
		'theme_color',
	]
	list_display = (
		'theme_color',
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

class BulletinEntryAdmin(admin.ModelAdmin):
	'''Bulletin Entry Admin Interface'''
	fields = [
		'enabled',
		'section',
		'position',
		'title',
		'value',
		'url',
		'additional_note',
		'bulletin_group',
	]
	list_display = (
		'enabled',
		'section',
		'position',
		'title',
		'value',
		'url',
		'additional_note',
		'bulletin_group',
	)
	actions = [make_enabled, make_disabled, make_inverted]


class BulletinEntryInline(admin.TabularInline):
	'''Bulletin Inline Admin Interface'''
	model = BulletinEntry
	extra = 0


class BulletinGroupAdmin(admin.ModelAdmin):
	'''Bulletin Group Admin Interface'''
	fields = [
		'name',
		'enabled',
	]
	inlines = [BulletinEntryInline]
	list_display = (
		'name',
		'enabled',
		'num_entries',
	)
	actions = [make_enabled, make_disabled, make_inverted]

admin.site.register(GeneralSettings, GeneralSettingsAdmin)
admin.site.register(MeetingTime, MeetingTimeAdmin)
admin.site.register(BulletinGroup, BulletinGroupAdmin)
admin.site.register(BulletinEntry, BulletinEntryAdmin)
