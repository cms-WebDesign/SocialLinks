# Generated by Django 3.2.9 on 2021-11-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialLinks', '0005_csseditor_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='csseditor',
            name='link_hover_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]