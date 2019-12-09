from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movie_list = Movie.objects.order_by('id')
    context = {'movie_list': movie_list}
    return render(request, 'film/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'film/detail.html', {'movie': movie})