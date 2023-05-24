from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import generics, permissions, status
from rest_framework.views import  APIView
from rest_framework.response import Response
from django.http import Http404
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
    

class MovieDetail(APIView):
    """
    Display details for a specific Movie.
    """

    serializer_class = MovieSerializer

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = self.serializer_class(movie)
        return Response(serializer.data)
    
