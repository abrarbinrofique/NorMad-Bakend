# Generated by Django 5.1.1 on 2024-09-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_travellerinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellerinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=15, null=True),
        ),
    ]
