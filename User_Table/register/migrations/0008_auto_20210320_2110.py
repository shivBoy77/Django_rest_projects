# Generated by Django 3.1.7 on 2021-03-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20210320_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='user_profile_pics/'),
        ),
    ]
