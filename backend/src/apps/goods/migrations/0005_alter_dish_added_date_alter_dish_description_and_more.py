# Generated by Django 4.0.4 on 2022-05-04 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_dish_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 12, 22, 55, 849164), verbose_name='Added'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available for users?'),
        ),
    ]