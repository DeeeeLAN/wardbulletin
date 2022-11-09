# Generated by Django 4.1.3 on 2022-11-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_generalsettings_homepage_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='alternate_homepage_photo',
            field=models.ImageField(blank=True, default='', help_text='Upload a photo here to set an alternate photo for the homepage.', upload_to='main/images/upload'),
            preserve_default=False,
        ),
    ]