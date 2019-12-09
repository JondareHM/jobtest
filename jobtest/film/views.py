from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, movie_id):
    return HttpResponse("You're looking at the movie %s." % question_id)