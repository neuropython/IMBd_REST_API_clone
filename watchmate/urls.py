from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watchlist/', include('watchlist_app.api.urls')),
    path('account/', include('userapp.api.urls')),
    # path('api-auth/', include('rest_framework.urls') , name='rest_framework')
]
