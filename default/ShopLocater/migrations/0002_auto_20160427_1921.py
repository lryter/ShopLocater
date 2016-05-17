# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_desc',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_name',
        ),
        migrations.AddField(
            model_name='task',
            name='coordinates',
            field=models.TextField(max_length=200, default='nothing'),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=200, default='nothing'),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, default='nothing'),
        ),
        migrations.AddField(
            model_name='task',
            name='pictures',
            field=models.FileField(upload_to='uploads/', default='nothing'),
        ),
    ]
