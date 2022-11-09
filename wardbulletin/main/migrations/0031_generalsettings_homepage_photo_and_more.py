# Generated by Django 4.1.3 on 2022-11-09 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_generalsettings_logo_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsettings',
            name='homepage_photo',
            field=models.FilePathField(blank=True, help_text='Path to the photo to be displayed on the homepage.\n\t\tIf not provided, the hompage will re-center the content without the image.', path='/opt/services/djangoapp/static/main/images', recursive=True),
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='homepage_quote',
            field=models.ForeignKey(blank=True, help_text='Select which quote in the quote table you want displayed under the picture on the homepage.\n\t\tDisabled quotes are allowed. If not provided, no quote will be displayed on the homepage.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quotes', to='main.quote'),
        ),
        migrations.AlterField(
            model_name='generalsettings',
            name='logo_path',
            field=models.FilePathField(blank=True, help_text='Path to the logo displayed in the top-left corner of the webpage.\n\t\tIf not provided, the corner will be left blank.', path='/opt/services/djangoapp/static/main/images', recursive=True),
        ),
        migrations.AlterField(
            model_name='generalsettings',
            name='photos_path',
            field=models.FilePathField(allow_folders=True, blank=True, help_text='Path to the directory containing the photos that will be displayed\n\t\trandomly on the program page. If not provided, the quote will be lonely.', path='/opt/services/djangoapp/static/main/images', recursive=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='url',
            field=models.CharField(blank=True, default='', help_text='Optional. The optional URL of the quote. If included, will add a hyperlink to the source field under the quote on the program page.', max_length=255),
        ),
    ]
