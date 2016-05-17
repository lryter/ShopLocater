# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0002_auto_20160427_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='coordinates',
            field=models.FloatField(default=0.0),
        ),
    ]
