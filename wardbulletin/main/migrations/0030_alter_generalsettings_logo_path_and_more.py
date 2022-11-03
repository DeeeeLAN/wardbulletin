# Generated by Django 4.1.3 on 2022-11-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_generalsettings_subscribe_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='logo_path',
            field=models.FilePathField(blank=True, help_text='Path to the logo displayed in the top-left corner of the webpage.\n\t\tIf not provided, the corner will be left blank.', path='/home/mariexse/public_html/static/main/images', recursive=True),
        ),
        migrations.AlterField(
            model_name='generalsettings',
            name='photos_path',
            field=models.FilePathField(allow_folders=True, blank=True, help_text='Path to the directory containing the photos that will be displayed\n\t\trandomly on the homepage. If not provided, the quote will be lonely.', path='/home/mariexse/public_html/static/main/images', recursive=True),
        ),
    ]
