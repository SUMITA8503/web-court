# Generated by Django 4.1.7 on 2023-04-11 07:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0006_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
    ]
