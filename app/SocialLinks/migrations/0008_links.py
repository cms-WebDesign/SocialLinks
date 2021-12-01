# Generated by Django 3.2.9 on 2021-11-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialLinks', '0007_auto_20211124_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link1', models.CharField(default='https://www.instagram.com', max_length=100)),
                ('link2', models.CharField(default='https://www.facebook.com', max_length=100)),
                ('link3', models.CharField(default='https://www.namecheap.com', max_length=100)),
                ('link4', models.CharField(default='mailto:email@gmail.com', max_length=100)),
                ('link5', models.CharField(default='https://www.contactme.com', max_length=100)),
                ('link6', models.CharField(default='https://www.link6.com', max_length=100)),
                ('link7', models.CharField(default='https://www.link7.com', max_length=100)),
            ],
        ),
    ]