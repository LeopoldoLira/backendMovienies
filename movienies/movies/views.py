from django.shortcuts import render
from .serializers import MovieSerializer, MovieRatingSerializer
from .models import Movie, MovieRating
from rest_framework import generics, permissions, status
from rest_framework.views import  APIView
from rest_framework.response import Response
from django.http import Http404
from .utils import RateMovie
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
    


class GetReview(generics.ListAPIView):
    """
    Listing all of the existing reviews.
    """

    serializer_class = MovieRatingSerializer

    def get_queryset(self):

        query_set = MovieRating.objects.all().order_by('-created_date')

        query_id_movie = self.request.query_params.get('idmovie', None)

        if query_id_movie is not None:
            try:
                query_id_movie = int(query_id_movie)
            except:
                query_id_movie = 0

            query_set = query_set.filter(movie__pk=query_id_movie)
        return query_set
    

class CreateReview(APIView):

    def __init__(self):
        self._rateMovie = RateMovie()

    serializer_class = MovieRatingSerializer
    permission_class = [permissions.IsAuthenticated]

    error = { 
            'response': ['You Already reviewed this movie.']
        }

    def put(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():

            isAlreadyAreview = MovieRating.objects.filter(movie_rated_owner__pk = request.user.pk, movie_rated__pk = serializer.validated_data['movie_rated'].pk).exists()

            if isAlreadyAreview:
                return Response(self.error, status = status.HTTP_400_BAD_REQUEST)
                
            instance = serializer.save(movie_rated_owner = self.request.user)
            self._rateMovie.setRate(instance)

            return Response(serializer.data, status = status.HTTP_200_OK)
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)