from django.db import models
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    avg_rating = models.FloatField(default=0)
    num_of_rating = models.IntegerField(default=0)
    
        
    def __str__(self):
        return self.name

class Review (models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    
    def __str__(self):
        return f"{self.rating} - {self.watchlist.name}"
    
