# Generated by Django 4.1.7 on 2023-03-16 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 16)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 16)),
        ),
    ]
