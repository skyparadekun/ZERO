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
    lastTime = models.DateTimeField()
    length = models.IntegerField()
    country = models.CharField(max_length=20)
    language = models.CharField(max_length=15)
    IMDb = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=40,blank=False)
    content = models.TextField()
    lastTime = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(default=0)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    lastTime = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=999,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+" "+self.text[0:7]