# Generated by Django 3.1.7 on 2021-03-10 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amlak',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 23, 23, 6, 334007)),
        ),
        migrations.AlterField(
            model_name='amlak',
            name='price',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
