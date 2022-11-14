'''Main app views'''
import datetime
from random import choice
from pathlib import Path
from django.shortcuts import render
from django.conf import settings
import markdown
from .models import GeneralSettings, BulletinGroup, ClassSchedule, Quote, Announcement, ContactTable
from .temple_photos_map import temples
import logging 

logger = logging.getLogger(__name__) 

header_theme_color_map = dict(
	slate   = '#e2e8f0',
	gray    = '#e5e7eb',
	zinc    = '#e4e4e7',
	neutral = '#e5e5e5',
	stone   = '#e7e5e4',
	brown   = '#eaddd7',
	red     = '#fecaca',
	orange  = '#fed7aa',
	amber   = '#fde68a',
	yellow  = '#fef08a',
	lime    = '#d9f99d',
	green   = '#bbf7d0',
	emerald = '#a7f3d0',
	teal    = '#99f6e4',
	cyan    = '#a5f3fc',
	sky     = '#bae6fd',
	blue    = '#bfdbfe',
	indigo  = '#c7d2fe',
	violet  = '#ddd6fe',
	purple  = '#e9d5ff',
	fuchsia = '#f5d0fe',
	pink    = '#fbcfe8',
	rose    = '#fecdd3',
)

md_client = markdown.Markdown(extensions=['smarty', 'md_in_html', 'pymdownx.magiclink', 'tables', 'nl2br'])

def get_default_context():
	'''Builds the initial context shared by all pages'''
	gs = GeneralSettings.objects.first()
	if gs:
		ward_name = gs.ward_name
		theme_color = gs.get_theme_color_display().lower()  # type: ignore
		logo_path = Path(gs.logo_path)
		if not logo_path.exists() or not logo_path.is_file():
			logo_path = ''
		else:
			logo_path = logo_path.relative_to(settings.BASE_DIR / 'main' / 'static')
	else:
		ward_name = 'Ward Bulletin'
		theme_color = 'brown'
		logo_path = ''

	css_file = 'all' if settings.DEBUG else theme_color

	header_theme_color = header_theme_color_map[theme_color]

	return {
		'ward_name': ward_name,
		'logo': logo_path,
		'theme_color': theme_color,
		'header_theme_color': header_theme_color,
		'css_file': css_file,
	}


def get_photo_paths(root):
	'''Recursively iterates over the provided path and returns
	a generator list of all files in the directory'''
	for path in root.glob('*'):
		if path.is_file():
			yield path
		else:
			yield from get_photo_paths(path)


# Create your views here.
def index(request):
	'''Index page'''

	image_path = ''
	image_name = ''
	quote = ''
	subscribe_email = ''
	media = False
	first_hour_meeting_time = None
	address = None
	gs = GeneralSettings.objects.first()
	if gs:
		if gs.alternate_homepage_photo != '':
			photo_path = Path(gs.alternate_homepage_photo.url)

			image_path = f'media{photo_path}'
			image_name = '_'.join(photo_path.stem.split('_')[:-1])
			media = True
				
		elif gs.homepage_photo != '':
			photo_path = Path(gs.homepage_photo)

			if photo_path.exists() and photo_path.is_file():
				image_path = photo_path.relative_to(settings.STATIC_ROOT)
				image_name = photo_path.stem

		if gs.homepage_quote and gs.homepage_quote != '':
			quote = gs.homepage_quote

		subscribe_email = gs.subscribe_email
		first_hour_meeting_time = gs.first_hour_meeting_time
		address = gs.meetinghouse_address


	context = get_default_context()
	context.update({
		'image': {
			'path': image_path,
			'name': image_name
		},
		'quote': quote,
		'first_hour_meeting_time': first_hour_meeting_time,
		'address': address,
		'media': media,
		'subscribe_email': subscribe_email,
	})
	return render(request, 'main/index.html', context)


def program(request):
	'''Program page'''


	bulletin_entries = None
	bulletin_group = BulletinGroup.objects.filter(enabled=True).first()
	if bulletin_group:
		bulletin_entries = bulletin_group.bulletinEntries.filter(enabled=True).order_by('position')  # type: ignore
		if bulletin_entries:
			for e in bulletin_entries:
				if e.raw_content != '':
					e.raw_content = md_client.convert(e.raw_content)


	class_entries = []
	class_groups = ClassSchedule.objects.filter(enabled=True).order_by('position')
	if class_groups:
		for group in class_groups:
			group_info = dict(
				title=group.title,
				schedule_date='',
				entries=[]
			)
			if group.schedule_date:
				group_info['schedule_date'] = group.schedule_date.strftime('%B %d, %Y')

			classes = group.classEntries.filter(enabled=True).order_by('position')
			for c in classes:
				if c.raw_content != '':
					c.raw_content = md_client.convert(c.raw_content)
			group_info['entries'] = classes

			class_entries.append(group_info)

	image_path = ''
	image_name = ''
	media = False
	first_hour_meeting_time = None
	second_hour_meeting_time = None
	meeting_date = None
	this_week = None
	gs = GeneralSettings.objects.first()
	if gs:
		if gs.alternate_photo != '':
			photo_path = Path(gs.alternate_photo.url)

			image_path = f'media{photo_path}'
			image_name = '_'.join(photo_path.stem.split('_')[:-1])
			media = True

		elif gs.photos_path != '':
			photos_path = Path(gs.photos_path)

			if photos_path.exists() and photos_path.is_file():
				image_path = photos_path.relative_to(settings.STATIC_ROOT)
				image_name = photos_path.stem

			elif photos_path.exists() and photos_path.is_dir():
				temple_images = [i.relative_to(settings.STATIC_ROOT) for i in get_photo_paths(photos_path)]
				image_path = choice(temple_images)
				image_name = image_path.stem
			
			rename = [t for t in temples if t['key'] == image_name]
			if len(rename) == 1:
				image_name = rename[0]['name']
		
		first_hour_meeting_time = gs.first_hour_meeting_time
		second_hour_meeting_time = gs.second_hour_meeting_time
		meeting_date = gs.get_next_meeting_date()
		this_week = ((datetime.datetime.strptime(meeting_date, '%B %d, %Y').day - 1) // 7 + 1) % 2


	quote_list = list(Quote.objects.filter(enabled=True))

	context = get_default_context()
	context.update({
		'image': {
			'path': image_path,
			'name': image_name
		},
		'media': media,
		'quote': choice(quote_list) if len(quote_list) > 0 else '',
		'meeting_date': meeting_date,
		'first_hour_meeting_time': first_hour_meeting_time,
		'second_hour_meeting_time': second_hour_meeting_time,
		'this_week': this_week,
		'sacrament_meeting_entries': bulletin_entries,
		'class_entries': class_entries,
	})
	return render(request, 'main/program.html', context)


def announcements(request):
	'''Announcements page'''

	context = get_default_context()

	announcement_qs = Announcement.objects.filter(enabled=True).order_by('position')
	
	context.update({
		'announcements': [md_client.convert(a.content) for a in announcement_qs],
	})
	return render(request, 'main/announcements.html', context)


def contacts_resources(request):
	'''Contacts/Resources page'''

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
