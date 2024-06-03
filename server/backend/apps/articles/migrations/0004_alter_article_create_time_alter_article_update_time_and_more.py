# Generated by Django 5.0.6 on 2024-06-03 07:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_created_at_article_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]
