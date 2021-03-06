# Generated by Django 4.0.4 on 2022-06-29 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_useraddress_mobile_and_more"),
        ("orders", "0002_remove_orderitem_order_order_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="ordered_by",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="user.customer"
            ),
        ),
    ]
