# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkthru_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipstricks',
            old_name='trick_text',
            new_name='tip_trick_text',
        ),
        migrations.AddField(
            model_name='tipstricks',
            name='tip_trick_author',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]
