from django.db.models import query
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Actor, Director, Genre
from .serializers import (ActorStatisticSerializer,
                          DirectorsStatisticSerializer,
                          MovieGenreStatisticSerializer)

class MovieGenreStatisticViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = MovieGenreStatisticSerializer


class ActorStatisticViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorStatisticSerializer


class DirectorStatisticViewSet(ReadOnlyModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorsStatisticSerializer