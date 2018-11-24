from django.urls import path
from . import views

urlpatterns = [
    path('signIn',views.signIn,name="signIn"),
    path('signUp',views.signUp,name="signUp"),
    path('getComment',views.getComment,name="getComment"),
    path('setComment',views.setComment,name="setComment"),
    path('getArticle',views.getArticle,name="getArticle"),
    path('getMovie',views.getMovie,name="getMovie"),
]