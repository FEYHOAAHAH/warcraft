# Generated by Django 4.2.8 on 2023-12-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='audio',
            field=models.FileField(upload_to='myapp/audios/'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to='myapp/videos/'),
        ),
    ]
