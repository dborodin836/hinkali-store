# Generated by Django 4.0.4 on 2022-05-04 08:33

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("orders", "0004_alter_order_ordered_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="id",
        ),
        migrations.RemoveField(
            model_name="order",
            name="ordered_by",
        ),
        migrations.AlterField(
            model_name="order",
            name="ordered_date",
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 11, 23, 44, 278613)),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "new order"),
                    ("pending", "pending order"),
                    ("finished", "finished order"),
                    ("canceled", "canceled order"),
                ],
                default="new",
                max_length=200,
            ),
        ),
        migrations.CreateModel(
            name="TemporaryOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ordered_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="user.customer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="temporaryorder_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="orders.temporaryorder",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.temporaryorder"
            ),
        ),
    ]
