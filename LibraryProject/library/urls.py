from django.urls import path
from . import views
from .views import AddBook, BookDetail, AddGenre, GenreDetail

urlpatterns = [
    path('books/', views.all_books, name='all_books'),
    path('addbook/', AddBook.as_view()),
    path('bookdetail/<int:pk>/', BookDetail.as_view()),
    path('addgenre/', AddGenre.as_view()),
    path('genredetail/<int:pk>/', GenreDetail.as_view())
]