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
    collector.set_book_genre('Книга', 'Фантастика')
    collector.add_book_in_favorites('Книга')
    return collector
