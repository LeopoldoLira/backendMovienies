from django.contrib import admin

from .models import Movie, MovieRating, MovieFavourites

# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieRating)
admin.site.register(MovieFavourites)