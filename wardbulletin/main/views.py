'''Main app views'''
import datetime
from random import choice
from pathlib import Path
from django.shortcuts import render
from django.conf import settings
import markdown
from .models import GeneralSettings, MeetingTime, BulletinGroup, Quote, Announcement, ContactTable

def get_default_context():
	gs = GeneralSettings.objects.first()
	if gs:
		theme_color = gs.get_theme_color_display().lower()  # type: ignore
		logo_path = Path(gs.logo_path)
		if not logo_path.exists() or not logo_path.is_file():
			logo_path = ''
		else:
			logo_path = logo_path.relative_to(settings.BASE_DIR.parent / 'main' / 'static')
	else:
		theme_color = 'brown'
		logo_path = ''

	return {
		'logo': logo_path,
		'theme_color': theme_color,
	}

# Create your views here.
def index(request):
	'''Index page'''

	mt = MeetingTime.objects.first()
	if mt:
		first_hour_meeting_time = mt.first_hour_meeting_time
		second_hour_meeting_time = mt.second_hour_meeting_time
		meeting_date = mt.get_next_meeting_date()
	else:
		first_hour_meeting_time = None
		second_hour_meeting_time = None
		meeting_date = None

	sacrament_meeting_entries = None
	sunday_school_entries = None
	relief_society_and_priesthood_entries = None
	bulletin_group = BulletinGroup.objects.filter(enabled=True).first()
	if bulletin_group:
		bulletin_entries = bulletin_group.bulletinEntries.filter(enabled=True).order_by('position')  # type: ignore
		if bulletin_entries:
			sacrament_meeting_entries = bulletin_entries.filter(section=1)
			sunday_school_entries = bulletin_entries.filter(section=2)
			relief_society_and_priesthood_entries = bulletin_entries.filter(section=3)

	image_path = ''
	image_name = ''
	gs = GeneralSettings.objects.first()
	if gs:
		if gs.photos_path != '':
			photos_path = Path(gs.photos_path)
			if photos_path.exists() and photos_path.is_file():
				image_path = photos_path.relative_to(settings.BASE_DIR.parent / 'main' / 'static')
				image_name = photos_path.stem
			elif photos_path.exists() and photos_path.is_dir():
				temple_images = [i.relative_to(settings.BASE_DIR.parent / 'main' / 'static') for i in photos_path.iterdir()]
				image_path = choice(temple_images)
				image_name = image_path.stem

	quote_list = list(Quote.objects.filter(enabled=True))

	context = get_default_context()
	context.update({
		'image': {
			'path': image_path,
			'name': image_name
		},
		'quote': choice(quote_list) if len(quote_list) > 0 else '',
		'meeting_date': meeting_date,
		'first_hour_meeting_time': first_hour_meeting_time,
		'second_hour_meeting_time': second_hour_meeting_time,
		'sacrament_meeting_entries': sacrament_meeting_entries,
		'sunday_school_entries': sunday_school_entries,
		'relief_society_and_priesthood_entries': relief_society_and_priesthood_entries,
	})
	return render(request, 'main/index.html', context)


def announcements(request):
	'''Announcements page'''

	announcement_qs = Announcement.objects.filter(enabled=True).order_by('position')
	md_client = markdown.Markdown(extensions=['smarty', 'md_in_html', 'pymdownx.magiclink', 'tables'])
	context = get_default_context()
	context.update({
		'announcements': [md_client.convert(a.content) for a in announcement_qs],
	})
	return render(request, 'main/announcements.html', context)


def contacts_resources(request):
	'''Contacts/Resources page'''

	md_client = markdown.Markdown(extensions=['smarty', 'md_in_html', 'pymdownx.magiclink', 'tables'])
	context = get_default_context()

	tables = ContactTable.objects.filter(enabled=True).order_by('position')
	tables = [{
		'heading': t.name,
		'contacts': t.contacts.all().order_by('position'),  # type: ignore
		'additional_notes': t.additional_notes,
		'markdown': md_client.convert(t.raw_content) if t.raw_content else ''
	} for t in tables]

	context.update({
		'contact_tables': tables,
	})

	return render(request, 'main/contacts-resources.html', context)
