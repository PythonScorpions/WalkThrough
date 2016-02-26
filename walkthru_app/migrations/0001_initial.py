# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoices',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answer_choice_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('article_image', models.FileField(upload_to='')),
                ('article_title', models.TextField()),
                ('article_desc', models.TextField()),
                ('article_author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question_text', models.CharField(max_length=500)),
                ('topic_fact', models.CharField(max_length=1000)),
                ('answer_description', models.CharField(max_length=500)),
                ('answer', models.ForeignKey(related_name='question_answer', to='walkthru_app.AnswerChoices')),
                ('answer_choices', models.ManyToManyField(related_name='question_answer_choices', to='walkthru_app.AnswerChoices')),
            ],
        ),
        migrations.CreateModel(
            name='TipsTricks',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tip_trick_date', models.DateField()),
                ('trick_text', models.CharField(max_length=1000)),
            ],
        ),
    ]
