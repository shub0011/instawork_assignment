# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('phone_number', models.CharField(max_length=15, null=True, blank=True)),
                ('role', models.CharField(blank=True, max_length=1, null=True, choices=[(b'A', b'Admin'), (b'R', b'Regular')])),
            ],
        ),
    ]
