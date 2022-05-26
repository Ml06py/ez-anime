from django.urls import path
from .views import (AvailableApiViews, TopRatedMovies, MovieDetail)

urlpatterns = [
    path("", AvailableApiViews.as_view(), name="available-api"),
    path("top/", TopRatedMovies.as_view(), name="top-movie-api"),
    path("movie-detail/<str:id>/", MovieDetail, name="film-detail-api"),
]