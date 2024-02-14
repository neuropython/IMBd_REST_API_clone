from django.urls import path
from django.urls import include
from .views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_details, name= 'movie_details' )
]
