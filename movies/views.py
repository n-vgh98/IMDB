from django.shortcuts import render
from django.http import HttpResponse
from movies.models import *
from .forms import MovieForm
from django.shortcuts import redirect, get_object_or_404


def movies_list(request):
    movies = Movie.objects.filter(is_valid=True)
    return render(request, 'movies/index.html', {'movies': movies})


def detail_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    genres = movie.genres
    movie_crew = MovieCrew.objects.filter(movie=movie).select_related('crew', 'role')
    directors = []
    writers = []
    actors = []
    for crew in movie_crew:
        if crew.role.title == 'director':
            directors.append(crew.crew.full_name)
        elif crew.role.title == 'Writer':
            writers.append(crew.crew.full_name)
        elif crew.role.title == 'actor':
            actors.append(crew.crew.full_name)

    return render(request, 'movies/detail.html',
                  {'movie': movie, 'directors': directors, 'writers': writers, 'actors': actors, 'genres': genres})


def create_movie(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, 'movies/create_form.html', {'form': form})
    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies_list')
        else:
            form = MovieForm()
            return render(request, 'movies/create_form.html', {'form': form})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk, is_valid=True)
    if request.method == 'GET':
        form = MovieForm(instance=movie)
        context = {
            'movie': movie,
            'form': form,
        }
        return render(request, 'movies/update_form.html', context=context)
    elif request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('detail_movie', pk=pk)
        else:
            form = MovieForm(instance=movie)
            context = {
                'movie': movie,
                'form': form,
            }
            return render(request, 'movies/update_form.html', context=context)


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.is_valid = False
    movie.save()

    return redirect('movies_list')


def rate_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    rating = MovieRate.objects.create(
        movie=movie,
        rate=int(request.POST.get('rate')),
        user=request.user,
    )
    rating.save()
    return redirect('movies_list')
