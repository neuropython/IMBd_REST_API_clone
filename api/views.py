from django.shortcuts import render
from watchlist_app.models import WatchList, StreamPlatform, Review
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import WatchListSerializer, StreamPlatformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import mixins
from rest_framework import generics
from .serializer import ReviewSerializer
from rest_framework import filters
from rest_framework import viewsets

# ------- Using ViewSet Class ---------

class StreamPlatformVS(viewsets.ViewSet):
    
    def list(self,request):
        data = StreamPlatform.objects.all()
        movies = StreamPlatformSerializer(data,many=True)
        return Response(movies.data)
    
    def create(self,request):
        movies = StreamPlatformSerializer(data=request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors)
    
    def retrieve(self,request,pk=None):
        data = StreamPlatform.objects.get(pk=pk)
        movies = StreamPlatformSerializer(data)
        return Response(movies.data)
    
    def update(self,request,pk):
        data = StreamPlatform.objects.get(pk=pk)
        movies = StreamPlatformSerializer(data, request.data)
        if movies.is_valid():
            movies.save()
            return Response(movies.data)
        else:
            return Response(movies.errors,status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        data = StreamPlatform.objects.get(pk=pk)
        data.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# ------- Using generic class ---------

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# ------- Using generic class with mixins ---------

# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)


# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# ------- Using APIView Class ---------

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
        