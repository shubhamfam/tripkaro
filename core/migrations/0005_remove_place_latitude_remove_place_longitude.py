# Generated by Django 4.0.3 on 2022-03-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_place_address_place_tag_alter_place_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='longitude',
        ),
    ]
