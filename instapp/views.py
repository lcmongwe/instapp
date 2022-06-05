from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from .forms import *

# authentication
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def home(request):
    profile=Profile.objects.all()

    posts=Image.objects.all()
    form=CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,('comment posted'))

    return render(request, 'home.html', {'posts': posts,'form': form,'profile':profile})



def comment(request,image_id):
    comment=Comment.objects.get(pk=image_id)
    form=CommentForm(request.POST )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html',{'comment':comment,'form':form})


def profile(request):
    profile=Profile.objects.all()
    return render(request, 'profile.html',{'profile': profile})

def post_picture(request):
    form=UploadImageForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,('picture posted'))

    return render(request, 'post.html',{'form': form,})

def create_profile(request):
    form=ProfileForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,('Profile created'))

    return render(request, 'create_profile.html',{'form': form,})


def update_profile(request,profile_id):
    profile=Profile.objects.get(pk=profile_id)
    form=ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('myprofile')
    return render(request, 'update_profile.html',{'profile':profile,'form':form})

def search_profile(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        profile=Profile.objects.filter(name__contains=searched)
        return render(request, 'searched.html',{'searched':searched,'profile':profile})
       

    else:
        return render(request, 'searched.html',{})





# AUTHENTICATION
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('there ws an error loggig in, please try again...'))
            return redirect('login')

    else:
        return render (request,'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,('you are logged out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Regestration succesful'))
            return redirect('home')
    else:
        form =RegisterUserForm()


    return render(request,'authenticate/register.html',{'form':form,})