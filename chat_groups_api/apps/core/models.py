from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User)
    created = models.DateTimeField()

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField()

    class Meta:
        ordering = ['created']
