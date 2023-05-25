from .models import MovieRating
from django.db.models import Sum

class RateMovie:
    
    def setRate(self, reviewRating: MovieRating):

        ratesSum = MovieRating.objects.filter(movie_rated__pk = reviewRating.movie_rated.pk).count()
        starsSum = MovieRating.objects.filter(movie_rated__pk = reviewRating.movie_rated.pk).aggregate(totalSum = Sum('movie_stars'))['totalSum'] or 0

        movie_score = 0

        if starsSum > 0:
            movie_score = ((starsSum * 20) / ratesSum)

            reviewRating.movie_rated.movie_score = movie_score
            reviewRating.movie_rated.save()