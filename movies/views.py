from django.shortcuts import render
from django.http import HttpResponse
from movies.models import *
from  .forms import MovieForm



def movies_list(request):
    movies = Movie.objects.filter(is_valid=True)
    return render(request, 'movies/index.html', {'movies': movies})


def detail_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    genres = movie.genres
    movie_crew = MovieCrew.objects.filter(movie=movie).select_related('crew', 'role')
    directors = []
    Writers = []
    actors = []
    for crew in movie_crew:
        if crew.role.title == 'director':
            directors.append(crew.crew.full_name)
        elif crew.role.title == 'Writer':
            Writers.append(crew.crew.full_name)
        elif crew.role.title == 'actor':
            actors.append(crew.crew.full_name)

    return render(request, 'movies/detail.html',
                  {'movie': movie, 'directors': directors, 'Writers': Writers, 'actors': actors, 'genres': genres})


def user_create_form(request):
    form = MovieForm()
    return render(request, 'movies/create_form.html', {'form': form})
