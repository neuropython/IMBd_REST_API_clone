from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name