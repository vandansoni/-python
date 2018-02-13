# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'FIve', b'5'), (b'six', b'6'), (b'seven', b'7'), (b'eight', b'8'), (b'nine', b'9'), (b'ten', b'10')]),
        ),
    ]
