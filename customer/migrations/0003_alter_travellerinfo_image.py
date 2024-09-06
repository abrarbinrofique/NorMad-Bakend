# Generated by Django 4.2.15 on 2024-09-05 11:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_traveller_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellerinfo',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
