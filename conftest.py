import pytest                                      
from main import BooksCollector

# Фикстура для создания нового экземпляра класса перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()

# Фикстура для создания предварительно заполненного экземпляра
@pytest.fixture
def populated_collector():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.books_genre['Война и мир'] = None
    collector.add_new_book('Книга')  # Сначала добавляем книгу
    collector.add_book_in_favorites('Книга')
    collector.books_genre = {
        "Война и мир": "Фантастика",
        "Гарри Поттер": "Фантастика",
        "Преступление и наказание": "Детективы",
        "12 стульев": "Комедии",
        "Оно": "Ужасы"
    }
    collector.books_genre = {
        "Книга1": "Фантастика",
        "Книга2": "Ужасы",
        "Книга3": "Фантастика",
        "Книга4": "Комедии",
        "Книга5": "Детективы"
    }

    return collector
