from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Vineet</h1>")


def about(request):
    return HttpResponse("vineet kumar")
