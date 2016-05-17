# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('task_name', models.CharField(max_length=20)),
                ('task_desc', models.TextField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
