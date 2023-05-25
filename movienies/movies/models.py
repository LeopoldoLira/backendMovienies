from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Movie(models.Model):
    movie_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_title = models.CharField(_('Movie\'s title'), max_length=255)
    movie_released_date = models.IntegerField(default=0000)
    movie_genre = models.CharField(max_length=255)
    movie_plot = models.TextField(blank=True, null=True)
    movie_image = models.ImageField(null=False, blank=False)
    movie_score = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.movie_title
    

class MovieRating(models.Model):
    movie_rated_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_rated = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_stars = models.IntegerField(default=1)
    movie_comment = models.CharField(null=True, blank=True, max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.movie_rated.movie_title}'


class MovieFavourites(models.Model):
    favourited_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favourited_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favourited_movie')

    def __str__(self):
        return f'{self.favourited_movie.movie_title} was favourited by {self.favourited_owner.username}'