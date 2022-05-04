# Generated by Django 4.0.3 on 2022-04-28 00:53

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('email', models.EmailField(max_length=254, verbose_name='Sender')),
                ('message', models.TextField(verbose_name="User's message")),
                ('added_date',
                 models.DateTimeField(default=datetime.datetime(2022, 4, 28, 0, 53, 43, 352997))),
            ],
        ),
    ]
