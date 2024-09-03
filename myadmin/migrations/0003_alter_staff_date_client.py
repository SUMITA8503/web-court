# Generated by Django 4.1.7 on 2023-03-14 07:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 14)),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date(2023, 3, 14))),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
