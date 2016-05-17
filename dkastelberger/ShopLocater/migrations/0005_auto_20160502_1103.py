# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0004_auto_20160502_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='coordinates',
            new_name='coordinatesx',
        ),
        migrations.AddField(
            model_name='task',
            name='coordinatesy',
            field=models.FloatField(default=0),
        ),
    ]
