from django.shortcuts import render
from rest_framework import generics

from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer


def all_books(request):
    books = Book.objects.all()
    return render(request, "all_books.html", {"books": books})


class AddBook(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AddGenre(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
