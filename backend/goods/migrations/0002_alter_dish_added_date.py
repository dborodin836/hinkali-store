# Generated by Django 4.0.3 on 2022-03-09 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 9, 10, 57, 20, 418926), verbose_name='Added'),
        ),
    ]
