from . import views
from django.urls import path, include

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movieDetails'),
    path('movies/create', views.CreatingMovie.as_view(), name='creatingMovie'),
    path('movies/update/<int:pk>', views.UpdatingMovie.as_view(), name='updatingMovie'),
    path('movies/delete/<int:pk>', views.DeleteMovie.as_view(), name='deleteMovie'),
    path('movies/reviews/<int:pk>', views.GetReview.as_view(), name='getReviews'),
    path('movies/reviews/create', views.CreateReview.as_view(), name='createReviews'),
    path('movies/favourites', views.GetFavourite.as_view(), name='getFavourites'),
    path('movies/favourites/<int:pk>', views.DeleteFavourite.as_view(), name='deleteFavourites'),
    path('movies/favourites/add', views.CreateFavourite.as_view(), name='createFavourites')
]

