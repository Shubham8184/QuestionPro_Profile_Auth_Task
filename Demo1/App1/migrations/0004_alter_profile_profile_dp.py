# Generated by Django 4.0 on 2021-12-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_dp',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
