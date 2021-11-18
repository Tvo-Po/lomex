import uuid

from django.db import models

from base_model import PersonModel


class Actor(PersonModel):
    pass


class Writer(PersonModel):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Movie(models.Model):
     
    id = models.CharField(primary_key=True, max_length=9) # TODO:validation
    
