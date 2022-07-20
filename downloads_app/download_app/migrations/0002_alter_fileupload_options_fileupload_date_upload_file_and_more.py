# Generated by Django 4.0.6 on 2022-07-14 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('download_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileupload',
            options={'verbose_name_plural': 'Upload file'},
        ),
        migrations.AddField(
            model_name='fileupload',
            name='date_upload_file',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]