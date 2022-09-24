from http.client import HTTPResponse
from operator import index
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')


