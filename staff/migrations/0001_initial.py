# Generated by Django 4.1.7 on 2023-03-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hearing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextdate', models.DateField()),
                ('remarks', models.TextField()),
                ('status', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.case')),
            ],
            options={
                'db_table': 'hearing',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('evidence', models.CharField(max_length=255)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.case')),
            ],
            options={
                'db_table': 'evidence',
            },
        ),
    ]
