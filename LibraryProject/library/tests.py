from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Genre, Book


class GenreModelTestCase(TestCase):
    def test_genre_creation(self):
        genre = Genre.objects.create(genre="Test Genre")
        self.assertEqual(genre.genre, "Test Genre")

    def test_genre_str(self):
        genre = Genre.objects.create(genre="Test Genre")
        self.assertEqual(str(genre), "Test Genre")

    def test_genre_unique(self):
        Genre.objects.create(genre="Test Genre")
        with self.assertRaises(IntegrityError):
            Genre.objects.create(genre="Test Genre")

    def test_genre_retrieve(self):
        genre = Genre.objects.create(genre="Test Genre")
        retrieve_genre = Genre.objects.get(genre="Test Genre")
        self.assertEqual(genre, retrieve_genre)


class BookModelTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre="Test Genre")

    def test_book_creation(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre=self.genre,
            isbn="123abc",
            available=True,
        )

        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.genre, self.genre)
        self.assertEqual(book.isbn, "123abc")
        self.assertTrue(book.available)

    def test_book_str(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre=self.genre,
            isbn="123abc",
            available=True,
        )

        self.assertEqual(str(book), "Test Book")
