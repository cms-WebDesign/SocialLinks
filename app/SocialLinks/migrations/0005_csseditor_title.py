# Generated by Django 3.2.9 on 2021-11-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialLinks', '0004_backgroundimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='csseditor',
            name='title',
            field=models.CharField(default='Home', max_length=20),
        ),
    ]