from . import views
from django.urls import path, include

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movies')
]