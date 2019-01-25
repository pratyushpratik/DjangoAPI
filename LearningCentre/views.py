from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LearningCentreCategories
from .serializers import LearningCentreCategoriesSerializer


# Create your views here.
class LearningCentreList(APIView):

    def get(self, request):
        snippet = get_list_or_404(LearningCentreCategories)
        serializer = LearningCentreCategoriesSerializer(snippet, many=True)
        return Response(serializer.data)
