from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return HttpResponse(render(request, "blog/home.html", context))

def about(request):
    return HttpResponse(render(request, "blog/about.html", {"title":"About"}))