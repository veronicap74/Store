from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):  
    if request.method == 'GET' :
      return render(request,'signup.html',{
        'form' : UserCreationForm,
    })
    else:       
        if request.POST['password1'] == request.POST['password2']:            
            try:
                 #register user
                user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(home)
                #return render(request,'tasks')
            except IntegrityError:   
                return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    'error':'El Usuario ya existe'
                }) 
        return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    'error':'Contreñas no coninciden'
                })     
