from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from Health.models import Contact, Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# from .forms import SignUpForm

# Create your views here.
# Home
def home(request):
  return render(request, 'home.html')
# About
def about(request):
  return render(request, 'about.html')

# Contact
def contact(request):
  print("inside contact ")
  if request.method == 'GET':
    return render(request, 'contact.html')
  if request.method=='POST':
    print("in contact ")
    username=request.POST['username']
    email=request.POST['email']
    phone=request.POST['phone']
    text=request.POST['text']
    Contact(username=username,email=email,phone=phone,text=text).save()
    print("contact hogay bhai ")
    return HttpResponse("Querry added <a href='/'>go to back</a> ")




  return render(request, 'contact.html')

# Services
def news(request):
  return render(request, 'news.html')



def profile(request):
  return render(request, 'profile.html')

# Logout
def user_logout(request):
  return HttpResponseRedirect('/')

#Signup
def user_signup(request):
 form = SignUpForm()
 return render(request, 'signup.html', {'form':form})

#Login
def user_login(request):
  return render(request, 'login.html')


def create(request):
  if request.method == 'GET':
    return render(request, 'createpost.html')
  if request.method == 'POST':
    title=request.POST['title']
    body=request.POST['body']
    Post(title=title,desc=body).save()
    return render(request, 'home.html')
    
def blogs(request):
  if request.method == 'GET':
    allBlogs = Post.objects.filter()
    theBlogs = []
    for blog in allBlogs:
      blogInstance = {
        "title": blog.title,
        "desc": blog.desc
      }
      theBlogs.append(blogInstance)
    return render(request, 'blogs.html', {
      "blogs": theBlogs
    })
  