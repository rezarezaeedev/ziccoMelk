# Generated by Django 3.1.7 on 2021-03-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20210304_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='profiles/%Y/%m/%d/'),
        ),
    ]
