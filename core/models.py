from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=455)
    password=models.CharField(max_length=255)
     
    def __str__(self):
        return self.username    

class Inferences(models.Model):
    name=models.CharField(max_length=255)
    channel_id=models.CharField(max_length=255)
    videoCount=models.IntegerField(default=0)
    subscriberCount=models.IntegerField(default=0)
    viewCount=models.IntegerField(default=0)
    description=models.CharField(max_length=255)
    publishedAt= models.DateTimeField()
    thumbnails=models.URLField()

    def __str__(self):
        return self.name

class Videos(models.Model):
    title=models.CharField(max_length=255)
    publishedAt=models.DateTimeField()
    thumbnails=models.URLField()
    video_id=models.CharField(max_length=255)
    viewCount=models.IntegerField()
    likeCount=models.IntegerField()
    commentCount=models.IntegerField()

    def __str__(self):  
        return self.title