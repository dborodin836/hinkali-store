# Generated by Django 4.0.4 on 2022-07-16 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0019_alter_dish_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vendor'),
        ),
    ]