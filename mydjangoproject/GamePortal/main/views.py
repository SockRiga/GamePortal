from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def guides(request):
    return render(request, 'main/guides.html')

def post1(request):
    return render(request, 'main/post1.html')

def post2(request):
    return render(request, 'main/post2.html')

def post3(request):
    return render(request, 'main/post3.html')

def guid1(request):
    return render(request, 'main/guid1.html')

def guid2(request):
    return render(request, 'main/guid2.html')