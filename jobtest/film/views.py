from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import RequestContext
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
	
def search(request):
	return render(request, 'film/search.html', {})
	
def register(request):
	movie = {}
	global movie_title
	global movie_genre
	global movie_poster
	if 'title' in request.POST:
		title = request.POST.get('title', '')
		url = 'http://www.omdbapi.com/?apikey=4e898dbb&t={0}'.format(title)
		response = requests.get(url)
		movie = response.json()
		if movie['Response'] == 'True':
			movie_title = movie['Title']
			movie_genre = movie['Genre']
			movie_poster = movie['Poster']
	if 'media' in request.POST:
		movie_media = request.POST.get('media')
		new_movie = Movie(title=movie_title, genre=movie_genre, poster=movie_poster, media=movie_media)
		new_movie.save()
		return redirect('index')
	return render(request, 'film/register.html', {'movie': movie})