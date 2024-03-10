from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Charley Kuchlenz",
        "title": "Blog Post 1",
        "content": "Blog post content",
        "date_posted": "March 8, 2024"
    },
    {
        "author": "Charley Kuchlenz",
        "title": "Blog Post 2",
        "content": "Blog post content 2",
        "date_posted": "March 8, 2024"
    },
    {
        "author": "Charley Kuchlenz",
        "title": "Blog Post 3",
        "content": "Blog post content 3",
        "date_posted": "March 8, 2024"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return HttpResponse(render(request, "blog/home.html", context))

def about(request):
    return HttpResponse(render(request, "blog/about.html", {"title":"About"}))