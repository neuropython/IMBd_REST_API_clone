from rest_framework import filters, mixins, serializers, status, viewsets, generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.models import WatchList, StreamPlatform, Review
from .serializer import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from .throttling import ReviewCreateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import WatchListPagination
# ------- Using ViewSet Class ---------

class SearchWatch(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description'] # @ is used to search in the description
                                              # field and i am using Postgres DB
    ordering_fields = ['avg_rating']


class UserReviewQuerry(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        return  Review.objects.filter(review_user__username=username)

class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        username = self.kwargs['username']
        return  Review.objects.filter(review_user__username=username)
    

class StreamPlatformVS(viewsets.ViewSet):
    permission_classes = [AdminOrReadOnly]
    
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
        movies = StreamPlatformSerializer(data, request.data, )
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] 
    queryset = Review.objects.none() # This is to avoid the error of "queryset not defined"
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        print(watchlist)
        
        current_user = self.request.user
        queryset = Review.objects.filter(watchlist=watchlist, review_user=current_user)
        
        if queryset.exists():
            raise serializers.ValidationError('You have already reviewed this movie')
        if watchlist.num_of_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            
        watchlist.num_of_rating = watchlist.num_of_rating + 1
        
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=current_user)
         

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    
    
    
    

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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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

class WatchListListGV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchListPagination
    
class WatchListListAV(APIView):
    permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAuthenticated]
    
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


# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     if request.method == 'GET':

#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)