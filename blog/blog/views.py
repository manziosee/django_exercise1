import re
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
import blog
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# 

@login_required(login_url='login')                  ##forces user to login before accessing any other page
def home(request):
    AllBlogs=Blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

@login_required(login_url='login')
def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

@login_required(login_url='login')
def likeBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('/')

@login_required(login_url='login')
def delBlog(request, id):
    blog=Blogs.objects.get(id=id)               ##objects are managers act intermediate
    blog.delete()
    return redirect("/")

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username1=request.POST.get('username')
            password1=request.POST.get('password')

            user=authenticate(request, username=username1, password=password1)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def register(request):
    form=CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' +user)
                return redirect('login')
    context={'form':form}
    return render(request, 'register.html', context)

def Blogupdate(request, pk):
    blog=Blogs.objects.get(id=pk)
    form = blogForm(instance=blog)
    if request.method=='POST':
        form=blogForm(request.POST, instance=blog)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    context={'form':form}
    return render(request, 'update.html', context)