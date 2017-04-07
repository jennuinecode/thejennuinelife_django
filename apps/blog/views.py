from django.shortcuts import render
from . models import Blog

def index(request):

    return render(request, 'blog/index.html')

def add(request):

    if request.method == "GET":

        return render(request, 'blog/add.html')
    else:

        Blog.objects.create(title=request.POST['title'],  category=request.POST['category'], entry=request.POST['entry'])

        context= {
            'blogs': Blog.objects.all()
        }

        return render(request, 'blog/index.html', context)


def delete(request, id):

    context= {
        'blogs': Blog.objects.filter(id=id)
    }
    course = Blog.objects.get(id=id)

    return render(request, 'blog/index.html', context)


def youcodegirl(request):

    return render(request, 'blog/posts/thegrind/youcodegirl.html')

def austinfoodietrip(request):

    return render(request, 'blog/posts/lifestyle/austinfoodietrip.html')

def fitnessstorypt1(request):

        return render(request, 'blog/posts/fitness/fitnessstorypt1.html')
