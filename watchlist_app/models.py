from django.db import models

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
        
    def __str__(self):
        return self.name
