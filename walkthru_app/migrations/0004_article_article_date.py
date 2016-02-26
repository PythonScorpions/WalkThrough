# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('walkthru_app', '0003_auto_20160226_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_date',
            field=models.DateField(default=datetime.date(2016, 2, 26)),
        ),
    ]
