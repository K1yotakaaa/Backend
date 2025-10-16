from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrReadOnly

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]
