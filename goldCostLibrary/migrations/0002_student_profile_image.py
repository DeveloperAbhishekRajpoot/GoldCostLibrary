# Generated by Django 5.1.1 on 2024-10-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldCostLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
