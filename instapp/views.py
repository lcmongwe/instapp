from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
# from .models import Article
# import datetime as dt
# from .forms import NewsLetterForm

# Create your views here.

def home(request):
    
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    return render(request, 'home.html', {})

