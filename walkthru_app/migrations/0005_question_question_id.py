# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkthru_app', '0004_article_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
