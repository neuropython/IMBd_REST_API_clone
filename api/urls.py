from django.urls import path
from django.urls import include
from .views import WatchListListAV, WatchListDetailsAV , StreamPlatformAV, StreamPlatformDetailsAV, ReviewList, ReviewDetails

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name= 'movie_details' ),
    path("stream_platform/", StreamPlatformAV.as_view(), name="stream_platform"),
    path("stream_platform/<int:pk>", StreamPlatformDetailsAV.as_view(), 
         name="stream_platform_details"),
        
    path('one/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path("one/review/<int:pk>", ReviewDetails.as_view(), name="review-details")
    
]
