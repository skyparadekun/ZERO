from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    poster = models.ImageField()
    name = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    producer = models.CharField(max_length=20)
    actor = models.CharField(max_length=40)
    kind = models.CharField(max_length=20)
    lastTime = models.TimeField()
    length = models.IntegerField()
    country = models.CharField(max_length=20)
    language = models.CharField(max_length=15)
    IMDb = models.CharField(max_length=15)
    

class Article(models.Model):
    title = models.CharField(max_length=40,blank=False)
    content = models.TextField()
    lastTime = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(default=0)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

class userProfile(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True)
    user = models.OneToOneField(User)

class Comment(model.Model):
    lastTime = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=999,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)