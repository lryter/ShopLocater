# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopLocater', '0005_auto_20160502_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[(1, 'Imbiss & Restaurant'), (2, 'Lebensmittel'), (3, 'Elektronik'), (4, 'Kleidung'), (5, 'Fahrzeug'), (6, 'Schmuck'), (7, 'Sport'), (8, 'Diverses')], default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='pictures',
            field=models.ImageField(upload_to='uploads/', default='uploads/fail.jpg'),
        ),
    ]
