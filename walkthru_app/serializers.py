from rest_framework import serializers

from .models import *


class AnswerChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoices


class QuestionSerializer(serializers.ModelSerializer):
    answer_choices = AnswerChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question_id', 'question_text', 'topic_fact', 'answer_choices')


class TipsAndTricksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipsTricks


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
