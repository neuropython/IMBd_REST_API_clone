from django.shortcuts import render
from watchlist_app.models import WatchList, StreamPlatform
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import WatchListSerializer, StreamPlatformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView 

class StreamPlatformAV(APIView):
    def get(self,request):
        data = StreamPlatform.objects.all()
        movies = StreamPlatformSerializer(data,many=True)
        return Response(movies.data)
    
    def post(self,request):
        movies = StreamPlatformSerializer(data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors)
        
class StreamPlatformDetailsAV(APIView):
    def get(self,request,pk):
        try:
            data = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        movies = StreamPlatformSerializer(data)
        return Response(movies.data)
        
    def put(self,request,pk):
        data = StreamPlatform.objects.get(pk=pk)
        movies = StreamPlatformSerializer(data, request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        data = StreamPlatform.objects.get(pk=pk)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
class WatchListListAV(APIView):
    def get(self,request):
        data = WatchList.objects.all()
        movies = WatchListSerializer(data,many=True)
        return Response(movies.data)
    
    def post(self,request):
        movies = WatchListSerializer(data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors)
                            
class WatchListDetailsAV(APIView):
    def get(self,request,pk):
        try:
            data = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        movies = WatchListSerializer(data)
        return Response(movies.data)
        
    def put(self,request,pk):
        data = WatchList.objects.get(pk=pk)
        movies = WatchListSerializer(data, request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        data = WatchList.objects.get(pk=pk)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)
        