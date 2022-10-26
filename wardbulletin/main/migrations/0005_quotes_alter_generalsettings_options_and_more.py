# Generated by Django 4.1.2 on 2022-10-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_generalsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(help_text='The source of the quote', max_length=128)),
                ('quote', models.TextField()),
                ('url', models.CharField(blank=True, default='', help_text='The optional URL of the quote', max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='generalsettings',
            options={'verbose_name': 'General Settings', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='bulletinentry',
            name='additional_note',
            field=models.CharField(blank=True, default='', help_text='If included, will show up next to the value (for example, the hymn number).', max_length=128),
        ),
        migrations.AlterField(
            model_name='bulletinentry',
            name='value',
            field=models.CharField(blank=True, default='', help_text='If added, will right-justify in-line with the (now left-justified) title.', max_length=128),
        ),
    ]
