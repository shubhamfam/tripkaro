# Generated by Django 4.0.3 on 2022-03-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_place_latitude_remove_place_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
