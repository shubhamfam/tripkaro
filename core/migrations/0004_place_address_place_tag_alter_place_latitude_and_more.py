# Generated by Django 4.0.3 on 2022-03-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_place_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='tag',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
