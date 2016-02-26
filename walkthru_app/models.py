from datetime import date

from django.db import models

# Create your models here.


class AnswerChoices(models.Model):

    answer_choice_text = models.CharField(max_length=500)

    def __str__(self):
        return "%s" % (self.answer_choice_text,)


class Question(models.Model):

    question_id = models.IntegerField()
    question_text = models.TextField()
    topic_fact = models.TextField()
    answer_description = models.TextField()
    answer = models.ForeignKey(AnswerChoices, related_name='question_answer')
    answer_choices = models.ManyToManyField(AnswerChoices, related_name='question_answer_choices')


class TipsTricks(models.Model):

    tip_trick_date = models.DateField()
    tip_trick_text = models.TextField(max_length=1000)
    tip_trick_author = models.CharField(max_length=100)


class Article(models.Model):

    article_image = models.FileField(upload_to='')
    article_title = models.TextField()
    article_desc = models.TextField()
    article_author = models.CharField(max_length=100)
    article_date = models.DateField(default=date.today())
