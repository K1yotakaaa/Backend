from django.urls import path
from .views import MovieListCreateAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
]
