from email.policy import HTTP
from django.shortcuts import render,HttpResponse
from urllib3 import HTTPResponse

def index(request):
    # return HttpResponse("<h1>Pradhumna Singh</h1> ")
    return render(request,'hiyu.html')

# Create your views here.
