from django.urls import path
from movies.views import movies_list


urlpatterns = [
    path('', movies_list, name='movies_list'),

]
