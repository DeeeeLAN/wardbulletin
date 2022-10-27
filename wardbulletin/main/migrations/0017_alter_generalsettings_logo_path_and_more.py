# Generated by Django 4.1.2 on 2022-10-27 08:14

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_generalsettings_logo_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='logo_path',
            field=models.FilePathField(blank=True, help_text='Path to the logo displayed in the top-left corner of the webpage.\n\t\tIf not provided, the corner will be left blank.', path=pathlib.PurePosixPath('/opt/services/djangoapp/src/wardbulletin/main/static/main/images'), recursive=True),
        ),
        migrations.AlterField(
            model_name='generalsettings',
            name='photos_path',
            field=models.FilePathField(allow_folders=True, blank=True, help_text='Path to the directory containing the photos that will be displayed\n\t\trandomly on the homepage. If not provided, the quote will be lonely.', path=pathlib.PurePosixPath('/opt/services/djangoapp/src/wardbulletin/main/static/main/images'), recursive=True),
        ),
    ]
