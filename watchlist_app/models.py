from django.db import models

class WatchList(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    time = models.DateTimeField()
        
    def __str__(self):
        return self.name

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name