from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import (WatchListListAV, 
                    WatchListDetailsAV ,
                    StreamPlatformAV, 
                    StreamPlatformDetailsAV, 
                    ReviewList, 
                    ReviewDetails, 
                    ReviewCreate, 
                    StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='stream')

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name= 'movie_details' ),
    
    # - Using multple url-s
    # path("stream_platform/", StreamPlatformAV.as_view(), name="stream_platform"),
    # path("stream_platform/<int:pk>", StreamPlatformDetailsAV.as_view(), 
    #      name="stream_platform_details"),
    
    # - Using single url
    path("", include(router.urls)),
        
    path('one/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('one/<int:pk>/review-create', ReviewCreate.as_view(), name='review-list'),
    path("one/review/<int:pk>", ReviewDetails.as_view(), name="review-details")
    
]
