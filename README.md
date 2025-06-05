# Project Overview 4 sprint
# BooksCollector is a Python application designed to manage a collection of books, including # their genres, favorites, and children’s books. This README focuses on the testing framework # and implemented test cases.
# Testing Framework
# Testing Library: pytest
# Fixtures:
# collector: creates a new instance of BooksCollector
# populated_collector: creates an instance with pre-added books
# Test Categories
# Add New Book Tests
# Empty Title Validation: checks if adding a book with an empty title fails
# Title Length Validation: verifies maximum allowed title length (40 characters)
# Duplicate Prevention: ensures only one instance of a book is added
# Parametrized Tests: covers various title scenarios with expected outcomes
# Set Book Genre Tests
# Valid Genre Assignment: checks correct genre assignment
# Invalid Genre Handling: tests response to non-existent genres
# Missing Book Handling: verifies behavior when setting genre for non-existent book
# Parametrized Tests: covers multiple genre assignment scenarios
# Children’s Books Tests
# Valid Children’s Book: confirms correct addition to children’s list
# Invalid Children’s Book: checks exclusion of non-children’s books
# Test Cases Details
# Add New Book
# test_add_new_book_empty_title: ensures no book is added with empty title
# test_add_new_book_too_long_title: validates title length limit
# test_add_new_book_max_length: checks maximum allowed title length
# test_add_new_book_duplicate: verifies duplicate prevention
# test_add_new_book_parametrized: parametrized test for various title scenarios
# Set Book Genre
# test_set_book_genre_valid: tests valid genre assignment
# test_set_book_genre_invalid_genre: checks invalid genre handling
# test_set_book_genre_missing_book: verifies handling of non-existent books
# test_set_book_genre_parametrized: parametrized test for genre assignment
# Children’s Books
# test_get_books_for_children_valid: confirms valid children’s book addition
# test_get_books_for_children_invalid: checks exclusion of non-children’s books
# Running Tests
# pytest test_books_collector.py

