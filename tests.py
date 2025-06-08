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
    def test_set_book_genre(self):
        # Проверяем успешное назначение жанра
        self.collector.set_book_genre('Война и мир', 'Фантастика')
        self.assertEqual(self.collector.books_genre['Война и мир'], 'Фантастика')

        # Проверяем назначение несуществующего жанра
        self.collector.set_book_genre('Война и мир', 'Фэнтези')
        self.assertIsNone(self.collector.books_genre['Война и мир'])

        # Проверяем назначение жанра для несуществующей книги
        self.collector.set_book_genre('1984', 'Фантастика')
        self.assertNotIn('1984', self.collector.books_genre)

    # Тесты для get_books_for_children
    def test_get_books_for_children_valid(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        assert 'Детская книга' in collector.get_books_for_children()

    def test_get_books_for_children_invalid(self, collector):
        collector.add_new_book('Детектив')
        collector.set_book_genre('Детектив', 'Детективы')
        assert 'Детектив' not in collector.get_books_for_children()

    def test_get_book_genre(self, populated_collector):
        # Проверяем получение жанра существующей книги
        book_name = "Гарри Поттер"
        expected_genre = "Фантастика"
        assert populated_collector.get_book_genre(book_name) == expected_genre

        # Проверяем обработку несуществующей книги
        book_name = "Неизвестная книга"
        assert populated_collector.get_book_genre(book_name) is None

        # Проверяем получение жанра для другой книги
        book_name = "Оно"
        expected_genre = "Ужасы"
        assert populated_collector.get_book_genre(book_name) == expected_genre

    # Проверка get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, populated_collector):
        collector.add_new_book("Книга1")  # добавляем первую книгу
        collector.add_new_book("Книга2")  # добавляем вторую книгу
        collector.set_book_genre("Книга1", "Фантастика")  # устанавливаем жанр
        collector.set_book_genre

    def test_get_books_genre(self, populated_collector):
        expected_dict = {
            "Война и мир": "Фантастика",
            "Гарри Поттер": "Фантастика",
            "Преступление и наказание": "Детективы",
            "12 стульев": "Комедии",
            "Оно": "Ужасы"
        }

        result_dict = populated_collector.get_books_genre()

        self.assertEqual(result_dict, expected_dict)
        self.assertEqual(populated_collector.books_genre, expected_dict)

        populated_collector.books_genre = {}
        self.assertDictEqual(populated_collector.get_books_genre(), {})

        # Тесты для favorites
    def test_add_book_in_favorites_valid(self, collector):
        # Добавляем книгу в избранное
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        # Проверяем, что книга есть в избранном
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_delete_from_favorites(self, collector):
        collector.add_new_book("Книга")  # добавляем книгу
        collector.add_book_in_favorites("Книга")  # добавляем в избранное
        collector.delete_book_from_favorites("Книга")  # удаляем из избранного
        # проверяем, что книга удалена
        assert "Книга" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        # Добавляем несколько книг в избранное
        collector.favorites.extend(["Война и мир", "Преступление и наказание", "Гарри Поттер"])

        # Получаем список избранных книг
        favorites_list = collector.get_list_of_favorites_books()

        # Проверяем, что метод возвращает список
        assert isinstance(favorites_list, list)

        # Проверяем, что все добавленные книги присутствуют в списке
        assert "Война и мир" in favorites_list
        assert "Преступление и наказание" in favorites_list
        assert "Гарри Поттер" in favorites_list

        # Проверяем длину списка
        assert len(favorites_list) == 3

