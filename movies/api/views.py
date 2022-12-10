from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from movies.models import *
from movies.api.serializers import *
from rest_framework.decorators import api_view, action
from django.shortcuts import redirect, get_object_or_404


@api_view(['GET', 'POST'])
def movies_list_api(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(is_valid=True)
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
def movie_detail_api(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movie.is_valid = False
        movie.save()
        return HttpResponse(status=204)
