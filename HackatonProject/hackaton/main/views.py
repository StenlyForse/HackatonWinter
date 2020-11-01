from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def citizens(request):
    return render(request, 'main/citizens.html')

def addComment(request):
    return render(request, 'main/addComment.html')