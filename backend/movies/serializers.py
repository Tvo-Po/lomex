from django.db.models import Avg, Count, Value
from django.db.models.functions import Concat, Round

from rest_framework import serializers

from .models import Actor, Director, Genre


class MovieGenreStatisticSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField('get_movies_count')
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    
    class Meta:
        model = Genre
        fields = ('name', 'movies_count', 'avg_rating')
    
    def get_movies_count(self, genre):
        return genre.movies.count()
    
    def get_avg_rating(self, genre):
        f_expression_for_rounded_rating = Round(Avg('imdb_rating') * 10) / 10
        return genre.movies.aggregate(
            avg_rate=f_expression_for_rounded_rating
        )['avg_rate']


class ActorStatisticSerializer(serializers.ModelSerializer):
    actor_name = serializers.SerializerMethodField('get_actor_name')
    movies_count = serializers.SerializerMethodField('get_movies_count')
    best_genre = serializers.SerializerMethodField('get_best_genre')
    
    class Meta:
        model = Actor
        fields = ('actor_name', 'movies_count', 'best_genre')
    
    def get_actor_name(self, actor):
        return str(actor)
    
    def get_movies_count(self, actor):
        return actor.movies.count()
    
    def get_best_genre(self, actor):
        actor_genres = actor.movies.values('genres')
        sorted_by_rating_actor_genres = actor_genres.annotate(
            avg_rate=Avg('imdb_rating')
        ).order_by('-avg_rate')
        try:
            top_genre = Genre.objects.get(
                id = sorted_by_rating_actor_genres[0]['genres']
            )
            return top_genre.name
        except IndexError:
            return None


class DirectorsStatisticSerializer(serializers.ModelSerializer):
    director_name = serializers.SerializerMethodField('get_director_name')
    favourite_actors = serializers.SerializerMethodField('get_favourite_actors')
    best_movies = serializers.SerializerMethodField('get_best_movies')
    
    class Meta:
        model = Director
        fields = ('director_name', 'favourite_actors', 'best_movies')
    
    def get_director_name(self, director):
        return str(director)
    
    def get_favourite_actors(self, director):
        actors_recorded_by_director = director.movies.values('actors')
        actors_frequency = actors_recorded_by_director.annotate(
            movies_count=Count('actors')
        ).order_by('-movies_count')
        actors_names = actors_frequency.annotate(name=Concat(
            'actors__first_name', Value(' '), 'actors__last_name'
        ))
        actors_queryset = actors_names.values('name', 'movies_count')
        actors_amount = len(actors_queryset)
        if actors_amount < 3:
            return actors_queryset[:actors_amount]
        return actors_queryset[:3]
    
    def get_best_movies(self, director):
        director_movies_rates = director.movies.values(
            'imdb_rating'
        ).order_by('-imdb_rating')
        top_movies_name = director_movies_rates.values('title')
        movies_amount = len(top_movies_name)
        if movies_amount < 3:
            return top_movies_name[:movies_amount]
        return top_movies_name[:3]