# Generated by Django 4.1.3 on 2022-11-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_classentry_additional_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='schedule_date',
            field=models.DateField(blank=True, help_text='Optional. If included, will appear below the title on the program.', null=True),
        ),
    ]
