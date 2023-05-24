from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import generics, permissions, status
from rest_framework.views import  APIView
from rest_framework.response import Response
# Create your views here.


class MovieList(generics.ListAPIView):

    """
    Display all avaialble movies available
    """

    serializer_class = MovieSerializer

    def get_queryset(self):

        movies_queryset = Movie.objects.all().order_by('-movie_released_date', '-movie_score')

        movie_query_title = self.request.query_params.get('movie_title')

        if movie_query_title is not None:
            movies_queryset = movies_queryset.filter(title__icontains=movie_query_title)
        
        return movies_queryset