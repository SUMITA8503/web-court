# Generated by Django 4.1.7 on 2023-04-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_appointment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
