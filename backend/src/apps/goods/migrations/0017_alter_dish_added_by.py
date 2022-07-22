# Generated by Django 4.0.4 on 2022-07-15 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_useraddress_mobile_and_more"),
        ("goods", "0016_alter_dish_added_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="added_by",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.vendor",
                verbose_name="Vendor",
            ),
            preserve_default=False,
        ),
    ]
