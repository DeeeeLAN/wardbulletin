# Generated by Django 4.1.3 on 2022-11-14 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_generalsettings_alternate_homepage_photo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MeetingTime',
        ),
        migrations.RemoveField(
            model_name='bulletinentry',
            name='section',
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='alternate_photo',
            field=models.ImageField(blank=True, help_text='Upload a photo here to set an alternate photo for the program.', upload_to=''),
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='first_hour_meeting_time',
            field=models.CharField(default='', help_text='Required. Your Sacrament Meeting meeting time.', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='meetinghouse_address',
            field=models.TextField(blank=True, help_text='Optional. Will display on the homepage if entered. Try and format it using 2-3 lines of text.'),
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='next_meeting_date',
            field=models.DateField(blank=True, help_text='Optional. The website automatically displays the next Sunday for the meeting date.\n\t\t\tSet a value here to override the next meeting date.', null=True),
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='second_hour_meeting_time',
            field=models.CharField(default='', help_text='Required. Your classes meeting time.', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bulletinentry',
            name='bulletin_group',
            field=models.ForeignKey(help_text='Required. Select which Bulletin Group this entry belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='bulletinEntries', to='main.bulletingroup'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_table',
            field=models.ForeignKey(help_text='Required. Select which Contact Table this contact belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='main.contacttable'),
        ),
    ]
