from datetime import date

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class QuestionList(APIView):

    def get(self, request, *args, **kwargs):
        question_id = self.kwargs['pk']
        questions = Question.objects.get(question_id=int(question_id))
        serializer = QuestionSerializer(questions)
        return Response({'data': serializer.data})


class QuestionAnswerSubmit(APIView):

    def post(self, request, *args, **kwargs):

        question_id = int(request.data['question_id'])
        answer_choice_id = int(request.data['answer_choice_id'])

        question_obj = Question.objects.get(id=question_id)

        response_data = {'answer_text': question_obj.answer_description, 'answer_id': question_obj.answer.id}

        if question_obj.answer_id == answer_choice_id:
            response_data['status'] = 1
        else:
            response_data['status'] = 0

        return Response(response_data)


class TipsAndTricks(APIView):

    def get(self, request, *args, **kwargs):
        today = date.today()
        tips_tricks = TipsTricks.objects.filter(tip_trick_date__gte=today)
        serializer = TipsAndTricksSerializer(tips_tricks, many=True)
        return Response({'data;': serializer.data})


class ArticleList(ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'data': serializer.data})
