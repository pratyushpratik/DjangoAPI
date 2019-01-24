from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


# Create your views here.
class StockList(APIView):

    def get(self, request):
        stock = get_list_or_404(Stock)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetails(APIView):

    def get_object(self, pk):
        return get_object_or_404(Stock, pk=pk)
        # try:
        #     return Stock.objects.get(pk=pk)
        # except Stock.DoesNotExist:
        #     raise Http404


    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StockSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StockSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        snippet = self.get_object(pk)
        serializer = StockSerializer(snippet, data=request.data,  partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
