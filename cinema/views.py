from rest_framework.viewsets import ModelViewSet

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession
from cinema.serializers import (
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieSessionSerializer
)


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
