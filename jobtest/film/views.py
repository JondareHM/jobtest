from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Movie
import json
import requests

def index(request):
    movie_list = Movie.objects.order_by('id')
    context = {'movie_list': movie_list}
    return render(request, 'film/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'film/detail.html', {'movie': movie})
	
def register(request):
    movie = {}
    if 'title' in request.GET:
        title = request.GET['title']
        url = 'http://www.omdbapi.com/?apikey=4e898dbb&t={0}'.format(title)
        response = requests.get(url)
        movie = response.json()
    return render(request, 'film/register.html', {'movie': movie})