from django.shortcuts import render
from watchlist_app.models import Movies
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        data = Movies.objects.all()
        movies = MovieSerializer(data,many=True)
        return Response(movies.data)
    
    elif request.method == 'POST':
        movies = MovieSerializer(data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors)
    


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            data = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        movies = MovieSerializer(data)
        return Response(movies.data)
    
    elif request.method == 'PUT':
        data = Movies.objects.get(pk=pk)
        movies = MovieSerializer(data, request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors,status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        data = Movies.objects.get(pk=pk)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)
