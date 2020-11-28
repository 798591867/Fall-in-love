from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "xinqiang/index.html", {})

def xiangce(request):
    return render(request, "xinqiang/photokuang.html", {})