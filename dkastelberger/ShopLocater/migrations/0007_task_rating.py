# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0006_auto_20160517_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], default=1),
        ),
    ]
