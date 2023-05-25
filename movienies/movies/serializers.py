from rest_framework import serializers

from .models import Movie, MovieRating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'pk',
            'movie_title',
            'movie_owner',
            'movie_released_date',
            'movie_genre',
            'movie_plot',
            'movie_image',
            'movie_score',
            'created_date',
            'updated_date'
        ]

        extra_kwargs = {
            'created_date': {'required': False},
            'update_date': {'required': False},
            'movie_owner': {'required': False},
            'movie_rate': {'required': False}
        }


class MovieRatingSerializer(serializers.ModelSerializer):
    movie_rated_owner = serializers.ReadOnlyField(source='movie_rated_owner.username')
    class Meta:
        model = MovieRating
        fields = [
            'pk',
            'movie_rated_owner',
            'movie_rated',
            'movie_stars',
            'movie_comment',
            'created_date',
            'updated_date'
        ]

        extra_kwargs = {
            'created_date':{'required':False },
            'updated_date':{'required':False },
            'movie_rated_owner': {'required': False}
        }