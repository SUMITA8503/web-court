# Generated by Django 4.1.7 on 2023-04-11 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_alter_client_date_alter_staff_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
    ]
