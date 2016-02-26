from django.contrib import admin

from .models import *
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('question_text',)


class AnswerChoiceAdmin(admin.ModelAdmin):
    model = AnswerChoices


class TipsTricksAdmin(admin.ModelAdmin):
    model = TipsTricks
    list_display = ('tip_trick_date', 'tip_trick_text', 'tip_trick_author')


class ArticleAdmin(admin.ModelAdmin):
    model = Article


admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerChoices, AnswerChoiceAdmin)
admin.site.register(TipsTricks, TipsTricksAdmin)
admin.site.register(Article, ArticleAdmin)
