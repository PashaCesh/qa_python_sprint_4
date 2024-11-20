import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_valid(self):
        collector = BooksCollector()
        collector.add_new_book("Доктор Живаго")
        assert "Доктор Живаго" in collector.books_genre

    def test_set_book_genre_add_new_book_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        assert collector.books_genre["Дюна"] == "Фантастика"

    def test_get_book_genre_add_new_book_set_genre_and_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        assert collector.get_book_genre("Сияние") == "Ужасы"

    def test_get_books_with_specific_genre_add_new_book_with_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Солярис")
        collector.set_book_genre("Солярис", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Солярис"]

    def test_get_books_genre_with_exist_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() != None

    def test_get_books_for_children_with_allowed_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Простоквашино")
        collector.set_book_genre("Простоквашино", "Мультфильмы")
        assert collector.get_books_for_children() == ["Простоквашино"]

    def test_get_books_for_children_with_restricted_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Убийство на улице Морг")
        collector.set_book_genre("Убийство на улице Морг", "Детективы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_valid_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        assert collector.get_list_of_favorites_books() == ["1984"]

    def test_delete_book_from_favorites_add_valid_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Незнайка на Луне")
        collector.add_book_in_favorites("Незнайка на Луне")
        collector.delete_book_from_favorites("Незнайка на Луне")
        assert collector.get_list_of_favorites_books() == []
