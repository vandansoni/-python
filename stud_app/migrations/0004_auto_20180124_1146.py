# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0003_auto_20180124_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
