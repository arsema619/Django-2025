from django.urls import path
from .views import (
    home,
    book_list,
    CreateLoanView,
    books_never_loaned_view,
    science_newton_books_view,
    top_members_view,
    books_per_category_view,
    book_list_json,
)

urlpatterns = [
    path('', home, name='home'),  # /
    path('books/', book_list, name='book_list'),  # /books/
    path('books/<int:book_id>/loan/', CreateLoanView.as_view(), name='create_loan'),

    path('never-loaned/', books_never_loaned_view, name='never_loaned'),
    path('science-books/', science_newton_books_view, name='science_books'),
    path('top-members/', top_members_view, name='top_members'),
    path('category-count/', books_per_category_view, name='category_count'),
    path('books/json/', book_list_json, name='book_list_json'),
]
