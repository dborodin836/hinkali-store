# Generated by Django 4.0.4 on 2022-05-04 09:58

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_alter_dish_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Added'),
        ),
    ]
