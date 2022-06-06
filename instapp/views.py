from django.urls import reverse

from email import message
from email.mime import image
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

# authentication
from django.shortcuts import render,redirect,get_object_or_404
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

    return render(request, 'home.html', {'posts': posts,'form': form,'profile':profile,})



def comment(request,image_id):
    comment=Comment.objects.get(pk=image_id)
    form=CommentForm(request.POST )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html',{'comment':comment,'form':form})


def like(request,post_id ):
    user = request.user
    post=Image.objects.get(id=post_id)
    current_likes= post.likes
    liked=Likes.objects.filter(user=user,image=post).count()
    if not liked:
        liked =Likes.objects.create(user=user,image=post)
        current_likes=current_likes +1
    else:
        liked =Likes.objects.create(user=user,image=post).delete()
        current_likes=current_likes -1

    post.likes=current_likes
    post.save()
    # return HttpResponseRedirect(reverse('home',args=[post_id]))
    return redirect('home')


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

            username=request.POST['username']
            email=request.POST['email']
            subject='welcome to InstaApp'
            message=f'Hi {username} welcome to InstaApp and have fun! '
            from_email=settings.EMAIL_HOST_USER
            recipients=[email]
            send_mail(subject, message,from_email,recipients,fail_silently=False)

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