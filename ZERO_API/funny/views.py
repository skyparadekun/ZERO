from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import json
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

@login_required
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

def getMovie(request):
