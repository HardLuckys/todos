# Generated by Django 2.2.2 on 2020-05-17 21:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todosapp', '0003_auto_20200517_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 0, 42, 13, 606295), verbose_name='Дата дедлайна'),
        ),
    ]
