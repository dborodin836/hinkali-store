# Generated by Django 4.0.4 on 2022-05-07 18:02

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='added_by',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='goods.dish'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='goods.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]