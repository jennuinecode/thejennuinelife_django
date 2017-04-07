from django.shortcuts import render, HttpResponse


def index(request):

    return render(request, 'website/index.html')

def about(request):

    return render(request, 'website/about.html')


def photography(request):

    return render(request, 'website/photography.html')


def design(request):

    return render(request, 'website/design.html')

def blog(request):

    return render(request, 'blog/index.html')

def contact(request):

    return render(request, 'website/contact.html')
