from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'pk',
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
