'''Main app views'''
import datetime
from django.shortcuts import render
from .models import GeneralSettings, MeetingTime, BulletinGroup

# Create your views here.
def index(request):
	'''Index page'''

	if GeneralSettings.objects.first():
		theme_color = GeneralSettings.objects.first().get_theme_color_display().lower()
	else:
		theme_color = 'brown'

	if MeetingTime.objects.first():
		first_hour_meeting_time = MeetingTime.objects.first().first_hour_meeting_time
		second_hour_meeting_time = MeetingTime.objects.first().second_hour_meeting_time
		meeting_date = MeetingTime.objects.first().get_next_meeting_date()
	else:
		first_hour_meeting_time = None
		second_hour_meeting_time = None
		meeting_date = None

	sacrament_meeting_entries = None
	sunday_school_entries = None
	relief_society_and_priesthood_entries = None
	bulletin_group = BulletinGroup.objects.filter(enabled=True).first()
	if bulletin_group:
		bulletin_entries = bulletin_group.bulletinEntries.filter(enabled=True).order_by('position')
		if bulletin_entries:
			sacrament_meeting_entries = bulletin_entries.filter(section=1)
			sunday_school_entries = bulletin_entries.filter(section=2)
			relief_society_and_priesthood_entries = bulletin_entries.filter(section=3)

	context = {
		'theme_color': theme_color,
		'meeting_date': meeting_date,
		'first_hour_meeting_time': first_hour_meeting_time,
		'second_hour_meeting_time': second_hour_meeting_time,
		'sacrament_meeting_entries': sacrament_meeting_entries,
		'sunday_school_entries': sunday_school_entries,
		'relief_society_and_priesthood_entries': relief_society_and_priesthood_entries,
	}
	return render(request, 'main/index.html', context)


def announcements(request):
	'''Announcements page'''

	context = {}
	return render(request, 'main/announcements.html', context)


def contacts_resources(request):
	'''Contacts/Resources page'''

	context = {}
	return render(request, 'main/contacts-resources.html', context)
