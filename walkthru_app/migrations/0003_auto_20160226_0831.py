# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkthru_app', '0002_auto_20160226_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic_fact',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tipstricks',
            name='tip_trick_text',
            field=models.TextField(max_length=1000),
        ),
    ]
