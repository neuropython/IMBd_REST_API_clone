from django.urls import path
from django.urls import include
from .views import WatchListListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name= 'movie_details' ),
    path("stream_platform/", StreamPlatformAV.as_view(), name="stream_platform"),
    path("stream_platform/<int:pk>", StreamPlatformDetailsAV.as_view(), name="stream_platform_details"),
]
