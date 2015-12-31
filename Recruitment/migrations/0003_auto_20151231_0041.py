# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0002_auto_20151225_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='apptype',
            name='frontpage_instructions',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 31, 0, 41, 38, 200132, tzinfo=utc)),
        ),
    ]
