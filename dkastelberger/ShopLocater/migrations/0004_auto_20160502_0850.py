# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0003_auto_20160429_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pictures',
            field=models.ImageField(default='nothing', upload_to='uploads/'),
        ),
    ]
