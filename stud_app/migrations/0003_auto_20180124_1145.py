# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0002_auto_20180124_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='contact',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='school',
            name='modified_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='rating',
            field=models.CharField(max_length=50, choices=[(b'one', b'1'), (b'two', b'2'), (b'three', b'3'), (b'four', b'4'), (b'five', b'5')]),
        ),
        migrations.AlterField(
            model_name='school',
            name='website',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='student',
            name='fees',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='modified_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='residence_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(max_length=50, choices=[(b'FIve', b'5'), (b'six', b'6'), (b'seven', b'7'), (b'eight', b'8'), (b'nine', b'9'), (b'ten', b'10')]),
        ),
    ]
