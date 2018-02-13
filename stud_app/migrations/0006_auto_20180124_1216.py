# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0005_auto_20180124_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='modified_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
