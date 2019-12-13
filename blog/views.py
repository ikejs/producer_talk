from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Ike',
        'title': 'Cool chord progression',
        'content': 'F Am C G',
        'date_posted': 'December 10th, 2019'
    },
    {
        'author': 'Bob',
        'title': 'Awesome melody',
        'content': 'C E G B G E C in eighth notes at 145 bpm!',
        'date_posted': 'December 11th, 2019'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)