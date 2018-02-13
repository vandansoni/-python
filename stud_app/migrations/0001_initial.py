# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('address', models.TextField()),
                ('rating', models.CharField(blank=True, max_length=50, null=True, choices=[(b'one', b'1'), (b'two', b'2'), (b'three', b'3'), (b'four', b'4'), (b'five', b'5')])),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('contact', models.IntegerField()),
                ('website', models.CharField(max_length=50)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('residence_address', models.TextField()),
                ('standard', models.CharField(blank=True, max_length=50, null=True, choices=[(b'six', b'6'), (b'seven', b'7'), (b'eight', b'8'), (b'nine', b'9'), (b'ten', b'10')])),
                ('roll_no', models.IntegerField(null=True, blank=True)),
                ('fees', models.CharField(max_length=50, null=True, blank=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('school', models.ForeignKey(to='stud_app.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
