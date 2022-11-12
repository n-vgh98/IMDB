from django.shortcuts import render
from django.http import HttpResponse

def movies_list(request):
    return render(request, 'movies/index.html')
