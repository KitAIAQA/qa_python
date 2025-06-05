from main import BooksCollector                        
import pytest
from fixtures import collector, populated_collector

class TestBooksCollector:
    # Тесты для add_new_book
    def test_add_new_book_empty_title(self, collector):
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_too_long_title(self, collector):
        collector.add_new_book('a' * 41)
        assert len(collector.books_genre) == 0

    def test_add_new_book_max_length(self, collector):
        collector.add_new_book('a' * 40)
        assert len(collector.books_genre) == 1

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.books_genre) == 1

    # Параметризация для add_new_book
    @pytest.mark.parametrize("title, expected_length", [
        ('', 0),
        ('a' * 41, 0),
        ('a' * 40, 1),
        ('Книга', 1),
        ('Книга', 1)
    ])
    def test_add_new_book_parametrized(self, collector, title, expected_length):
        collector.add_new_book(title)
        assert len(collector.books_genre) == expected_length

    # Тесты для set_book_genre
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Неизвестный жанр')
        assert collector.get_book_genre('Книга') == ''

    def test_set_book_genre_missing_book(self, collector):
        collector.set_book_genre('НетВСписке', 'Фантастика')
        assert collector.get_book_genre('НетВСписке') is None

    # Параметризация для set_book_genre
    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ('Книга', 'Фантастика', 'Фантастика'),
        ('Книга', 'Неизвестный жанр', ''),
        ('НетВСписке', 'Фантастика', None)
    ])
    def test_set_book_genre_parametrized(self, collector, book_name, genre, expected_genre):
        if book_name != 'НетВСписке':
            collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    # Тесты для get_books_for_children
    def test_get_books_for_children_valid(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        assert 'Детская книга' in collector.get_books_for_children()

    def test_get_books_for_children_invalid(self, collector):
        collector.add_new_book('Детектив')
        collector.set_book_genre('Детектив', 'Детективы')
        assert 'Детектив' not in collector.get_books_for_children()


