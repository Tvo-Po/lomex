from django.contrib import admin

from .models import Actor, Director, Genre, Movie, Writer


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title', )

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'id')
    search_fields = ('first_name', 'id')