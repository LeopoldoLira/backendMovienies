from django.shortcuts import render
from .serializers import MovieSerializer, MovieRatingSerializer, FavouritedMovieSerializer
from .models import Movie, MovieRating, MovieFavourites
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

    def get(self, request, pk, format = None):
        review = MovieRating.objects.filter(movie_rated = pk)
        serializer = self.serializer_class(review, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class CreateReview(APIView):

    def __init__(self):
        self._rateMovie = RateMovie()

    serializer_class = MovieRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    

class GetFavourite(APIView):
    """
    Get the favourited movies from a user.
    """

    serializer_class = FavouritedMovieSerializer
    permissions_class = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        favourite = MovieFavourites.objects.filter(favourited_owner = request.user.id)
        serializer = self.serializer_class(favourite, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class CreateFavourite(APIView):
    """
    Create a favourite for the user.
    """
    serializer_class = FavouritedMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        pk = request.data.get('movie_id', None)
        
        if pk == None:
            return Response({'response':'Please provide an ID'}, status = status.HTTP_400_BAD_REQUEST)
        
        movie_exists = Movie.objects.filter(id = pk).exists()
        if not movie_exists:
            return Response({'response':'Movie does not Exists'}, status = status.HTTP_400_BAD_REQUEST)

        favourite_exists = MovieFavourites.objects.filter(favourited_owner = request.user.id, favourited_movie_id = pk).exists()
        if not favourite_exists:
            serializer = self.serializer_class(data={'favourited_movie':pk, 'favourited_owner':request.user.id}) 
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'response': 'favourite added successfully.','status':2000}, status = status.HTTP_200_OK)
        return Response(data={'response':'Favourited is already added', 'status':2001}, status = status.HTTP_200_OK)
        

class DeleteFavourite(APIView):
    """
    Delete a Favourite from the users's account.
    """

    serializer_class = FavouritedMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        
        favourite = MovieFavourites.objects.filter(favourited_owner = request.user.id, id=pk)
        if favourite.exists():
            favourite.delete()
            return Response({'response':'Favourite Sucessfully deleted.'}, status = status.HTTP_200_OK)
        else:
            return Response({'response':'Favourite Does not exists'}, status = status.HTTP_404_NOT_FOUND)
    

class CreatingMovie(APIView):
    """
    Creating a Movie.
    """

    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(movie_owner = self.request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UpdatingMovie(APIView):
    """
    Updating a specific Movie
    """

    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = self.serializer_class(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DeleteMovie(APIView):

    """
    Delete a Specific Movie.
    """

    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
        
    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(data={'Movie status':'Deleted'}, status = status.HTTP_200_OK)