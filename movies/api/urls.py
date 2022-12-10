from django.urls import path
from movies.api.views import *

urlpatterns = [
    path('movies/', movies_list_api, name='movies_list_api'),
    path('movie/<int:pk>', movie_detail_api, name='movie_detail_api')

]
