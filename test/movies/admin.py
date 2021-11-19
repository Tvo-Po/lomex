from django.contrib import admin

from .models import Actor, Director, Genre, Movie, Writer


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Movie)
admin.site.register(Genre)
