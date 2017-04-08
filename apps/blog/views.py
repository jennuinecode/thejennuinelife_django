from django.shortcuts import render
from . models import Blog

def index(request):

    return render(request, 'blog/index.html')


def youcodegirl(request):

    return render(request, 'blog/posts/thegrind/youcodegirl.html')

def myphotographystory(request):

    return render(request, 'blog/posts/thegrind/myphotographystory.html')


def fitnessstorypt1(request):

        return render(request, 'blog/posts/fitness/fitnessstorypt1.html')
