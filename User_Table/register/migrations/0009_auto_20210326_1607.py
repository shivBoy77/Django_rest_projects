# Generated by Django 3.1.7 on 2021-03-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20210320_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/user_profile_pics/default.jpg', null=True, upload_to='user_profile_pics/'),
        ),
    ]
