from django.shortcuts import render
from django.http import HttpResponse


# Create your views here. This is the VIEW from the MVT architecture

def index(request):
    return HttpResponse('<h1>Asia Tours Agency</h1><br><p>Successfully created!</p>')
