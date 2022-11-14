from django.urls import path
from movies.views import *


urlpatterns = [
    path('', movies_list, name='movies_list'),
    path('detail/<int:pk>', detail_movie, name='detail_movie'),
    path('show_form_create/', show_create_form, name='show_create_form'),

]
