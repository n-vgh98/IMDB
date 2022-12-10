from django.urls import path
from movies.api import views

urlpatterns = [
    path('movies/', views.MoviesList.as_view(), name='movies_list_api'),
    # path('movie/<int:pk>', movie_detail_api, name='movie_detail_api')

]
