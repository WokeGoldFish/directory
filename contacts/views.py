
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
#import all of your models

from .models import Post
from django.contrib import messages

#import all your forms 

from .forms import PostForm

from django.contrib.auth.forms import UserCreationForm


# def index(request):
#     posts = Post.objects.all()
    
#     context = {'posts':posts}
#     return render(request, 'pokemon/homepg.html', context={})

def homePg(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    return render(request, 'contacts/homepage.html', context=context)

def about(request):
    return render(request, 'contacts/about.html', context={})


def createPost(request):
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
    else:
        print('get req submitted', request.method)
        
    return render(request, 'contacts/createpost.html', context= {'form':form})


def signIn(request):
    return render(request, 'contacts/signin.html', context = {})

def signUp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, f'Account Created {user}!')
            return redirect('signin')
        else:
            messages.warning(request, f'Invalid Attempt')
            print('invalid', form.errors)
    else:
        print('get req submitted', request.method)
        
    return render(request, 'contacts/signup.html', context = {'form':form})