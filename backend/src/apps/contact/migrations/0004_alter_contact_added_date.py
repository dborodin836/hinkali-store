# Generated by Django 4.0.4 on 2022-05-04 09:22

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 12, 22, 55, 860163)),
        ),
    ]
