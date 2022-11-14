from django.urls import path
from movies.views import *


urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('detail/<int:pk>', detail_movie, name='detail_movie'),
    path('create_movie/', create_movie, name='create_movie'),
    path('edit_movie/<int:pk>', edit_movie, name='edit_movie'),
    path('delete_movie/<int:pk>', delete_movie, name='delete_movie'),


]
