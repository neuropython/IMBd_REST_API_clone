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
                    StreamPlatformVS,
                    UserReview,
                    UserReviewQuerry,
                    SearchWatch,
                    WatchListListGV)

router = DefaultRouter()
# router is used to generate urls for the viewset avoiding many lines of code for same urls
router.register('stream', StreamPlatformVS, basename='stream')

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name= 'movie_details' ),
    
    # - Using multple url-s
    # path("stream_platform/", StreamPlatformAV.as_view(), name="stream_platform"),
    # path("stream_platform/<int:pk>", StreamPlatformDetailsAV.as_view(), 
    #      name="stream_platform_details"),
    
    # ---Using single url---
    path("", include(router.urls)),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    
    # ---Different filtering methods---
    path("review/<int:pk>/", ReviewDetails.as_view(), name="review-detail"),
    path("reviews/<str:username>/", UserReview.as_view(), name="user-review-detail"),
    path("reviews/", UserReviewQuerry.as_view(), name="querry-review-detail"),
    path("search/", SearchWatch.as_view(), name="querry-review-detail"),
    path('pagination/', WatchListListGV.as_view(), name='movie-list-paginated')
    
    
    
]
