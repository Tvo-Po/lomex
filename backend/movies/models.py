import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import SET_NULL

from .base_model import PersonModel


class Actor(PersonModel):
    pass


class Director(PersonModel):
    pass


class Writer(PersonModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
     
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=150)
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField(blank=True)
    genres = models.ManyToManyField('Genre', related_name='movies')
    directors = models.ManyToManyField('Director', related_name='movies')
    writers = models.ManyToManyField('Writer', related_name='movies')
    actors = models.ManyToManyField('Actor', related_name='movies')
    
    def __str__(self):
        return self.title
    
    def clean(self):
        self.id = self.id.replace(' ', '')
        if len(self.id) < 9:
            raise ValidationError(
                {'id': 'ID should be at least 9 symbols lenght without spaces'}
            )
        if self.id[:2] != 'tt':
            raise ValidationError(
                {'id': 'ID shold start with "tt"'}
            )
        try:
            int(self.id[2:])
        except ValueError:
            raise ValidationError(
                {'id': 'The rest part of ID should be numbers'}
            )
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    @property
    def genre(self):
        composite_genre = ''.join([str(genre) for genre in self.genres])
        return composite_genre
    
    @property
    def actors_names(self):
        names = ''.join([str(actor) for actor in self.actors])
        return names
    
    @property
    def writers_names(self):
        names = ''.join([str(writer) for writer in self.writers])
        return names
