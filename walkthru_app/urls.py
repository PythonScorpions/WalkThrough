from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionList.as_view(), name='questions-list'),
        url(r'^question_answer_submit/$', views.QuestionAnswerSubmit.as_view(), name='question-answer-submit'),
        url(r'^tips_tricks/$', views.TipsAndTricks.as_view(), name='tips-tickets'),
        url(r'^articles/$', views.ArticleList.as_view(), name='articles')
]
