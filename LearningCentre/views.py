from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LearningCentreCategories, LearningCentreSubCategories, LearningCentreSubCategoriesQuestionAnswer
from .serializers import LearningCentreCategoriesSerializer, LearningCentreSubCategoriesQuestionsAnswersWithSubcategoryIDSerializer, LearningCentreSubCategoriesQuestionAnswerSerializer
from django.core.paginator import Paginator


# Create your views here.
class LearningCentreList(APIView):

    def get(self, request):
        snippet = get_list_or_404(LearningCentreCategories)
        serializer = LearningCentreCategoriesSerializer(snippet, many=True)
        return Response(serializer.data)


class GetLearningCentreQuestionsAnswersWithSubcategoryID(APIView):

    def get(self, request, pk):
        snippet = get_list_or_404(LearningCentreSubCategoriesQuestionAnswer, subcategory_id=pk)

        limit = request.GET.get('limit')
        paginator = Paginator(snippet, limit)

        page = request.GET.get('page')
        snippet2 = paginator.get_page(page)

        serializer = LearningCentreSubCategoriesQuestionAnswerSerializer(snippet2, many=True)
        return Response({'result': serializer.data, 'count': len(snippet), 'next': snippet2.has_next()})


