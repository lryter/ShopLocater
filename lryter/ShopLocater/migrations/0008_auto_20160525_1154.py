# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0007_task_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[(1, 'Gastronomie'), (2, 'Lebensmittel'), (3, 'Elektronik'), (4, 'Textil/Fashion'), (5, 'Fahrzeug'), (6, 'Schmuck'), (7, 'Fitness/Sport'), (8, 'Beauty/Wellness'), (9, 'Abenteuer/Freizeit'), (10, 'Bildung'), (11, 'Diverses')], default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=200, default='description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, default='Shopname'),
        ),
    ]
