from cgitb import html
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePg, name= 'home'),
    path('home/', views.homePg, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('createpost/', views.createPost, name= 'createpost'),
    path('signin/', views.signIn, name= 'signin'),
    path('signup/', views.signUp, name= 'signup'),
]