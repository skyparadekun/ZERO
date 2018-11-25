from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http import JsonResponse
from json import dumps
from django.core import serializers
from .models import *
import datetime
# Create your views here.

def signIn(request):
    value={}
    if(request.method=='POST'):
        #没有防注入
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
                auth.login(request, user)
                value['code']=1
                value['status']='Success!'
                value['info']=list(User.objects.get(username=username))
                return HttpResponse(json.dumps(value),content_type="application/json")
        else:
            value['code']=0
            value['status']='Invalid User!'
            return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']="Can't visit the API in this way!"
        return HttpResponse(json.dumps(value),content_type="application/json")

def signUp(request):
    value={}
    if(request.method=='POST'):
        #没有防注入
        email = request.POST.get('email','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username):
            value['code']=0
            value['status']='Username has existed!'
            return HttpResponse(json.dumps(value),content_type="application/json")
        else:
            user = User()
            user.set_password(password)
            user.username=username
            user.email=email
            user.save()
            newUser=auth.authenticate(username=username,password=password)
            if newUser is not None and newUser.is_active:
                auth.login(request, user)
                value['code']=1
                value['status']='Success!'
                return HttpResponse(json.dumps(value),content_type="application/json")
            else:
                value['code']=0
                value['status']='Invalid User!'
                return HttpResponse(json.dumps(value),content_type="application/json")

def signOut(request):
    value={}
    if request.user.is_active:
        auth.logout(request)
        value['code']=1
        value['status']='Success!'
        return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']='You have no right to access this API!'
        return HttpResponse(json.dumps(value),content_type="application/json")

def getComment(request):
    value={}
    if request.method=="GET":
        articleId = request.GET.get('articleId','')
        article = Article.objects.get(id=articleId)
        comments = Comment.objects.filter(article=article)
        Info=[]
        for comment in comments:
            Info.append(model_to_dict(comment))
        value['info']=Info
        value['code']=1
        value['status']='Success!'
        return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']="Can't visit the API in this way!"
        return HttpResponse(json.dumps(value),content_type="application/json")

@login_required()
def setComment(request):
    value={}
    if request.user.is_active:
        if(request.method=='POST'):
            text = request.POST.get('text','')
            articleId = request.POST.get('articleId','')
            comment = Comment()
            comment.article=Article.objects.get(id=articleId)
            comment.user=request.user
            comment.text=text
            comment.lastTime=datetime.Now()
            comment.save()
        else:
            value['code']=0
            value['status']="Can't visit the API in this way!"
            return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']='You have no right to access this API!'
        return HttpResponse(json.dumps(value),content_type="application/json")

def getArticle(request):
    value={}
    if request.method=="GET":
        movieId = request.GET.get('movieId','')
        movie = Movie.objects.get(id=movieId)
        articles = Article.objects.filter(movie=movie)
        Info=[]
        for article in articles:
            Info.append(model_to_dict(article))
        value['info']=Info
        value['code']=1
        value['status']='Success!'
        return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']="Can't visit the API in this way!"
        return HttpResponse(json.dumps(value),content_type="application/json")

def getMovie(request):
    value={}
    if request.method=="GET":
        movies = Movie.objects.all()
        Info=[]
        for movie in movies:
            Info.append(model_to_dict(movie))
        value['info']=Info
        value['code']=1
        value['status']='Success!'
        return HttpResponse(json.dumps(value),content_type="application/json")
    else:
        value['code']=0
        value['status']="Can't visit the API in this way!"
        return HttpResponse(json.dumps(value),content_type="application/json")