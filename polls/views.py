from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return HttpResponse("Hello, home. You're at the polls index.")


def dom(request):
    return HttpResponse("Hello, dom. You're at the polls index.")
