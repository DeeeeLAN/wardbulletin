# Generated by Django 4.1.3 on 2022-11-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_meetingtime_meetinghouse_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='alternate_homepage_photo',
            field=models.ImageField(blank=True, help_text='Upload a photo here to set an alternate photo for the homepage.', upload_to='media'),
        ),
    ]