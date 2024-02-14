from django.shortcuts import render
from watchlist_app.models import Movies
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView 


class MovieListAV(APIView):
    def get(self,request):
        data = Movies.objects.all()
        movies = MovieSerializer(data,many=True)
        return Response(movies.data)
    
    def post(self,request):
        movies = MovieSerializer(data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors)
                            
class MovieDetailsAV(APIView):
    def get(self,request,pk):
        try:
            data = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        movies = MovieSerializer(data)
        return Response(movies.data)
        
    def put(self,request,pk):
        data = Movies.objects.get(pk=pk)
        movies = MovieSerializer(data, request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        data = Movies.objects.get(pk=pk)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)
        