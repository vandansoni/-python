# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0004_auto_20180124_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='modified_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
