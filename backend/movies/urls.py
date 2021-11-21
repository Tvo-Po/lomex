from django.urls import path

from .views import (DirectorStatisticViewSet,
                    MovieGenreStatisticViewSet,
                    ActorStatisticViewSet)

urlpatterns = [
    path('genres/', MovieGenreStatisticViewSet.as_view({'get': 'list'})),
    path('actors/', ActorStatisticViewSet.as_view({'get': 'list'})),
    path('directors/', DirectorStatisticViewSet.as_view({'get': 'list'}))
]
