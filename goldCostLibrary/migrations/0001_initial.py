# Generated by Django 5.1.1 on 2024-10-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('seat_number', models.CharField(max_length=10)),
                ('joining_date', models.DateField()),
                ('monthly_fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]