from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def new_post(request):
    return render(request, 'main/new_post.html')

def new(request):
    return render(request, 'main/new_post.html')

def page1(request):
    return render(request, 'main/page1.html')

def page2(request):
    return render(request, 'main/page2.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')
