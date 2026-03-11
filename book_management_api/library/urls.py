from django.urls import path
from . import views

urlpatterns = [

# Author APIs
path("authors/", views.authors_list),
path("authors/<int:id>/", views.author_detail),
path("authors/create/", views.create_author),
path("authors/<int:id>/update/", views.update_author),
path("authors/<int:id>/delete/", views.delete_author),
path("authors/<int:id>/books/", views.books_by_author),
path("authors/book-count/", views.author_book_count),

# Book APIs
path("books/", views.books_list),
path("books/<int:id>/", views.book_detail),
path("books/create/", views.create_book),
path("books/<int:id>/update/", views.update_book),
path("books/<int:id>/delete/", views.delete_book),

# Filtering
path("books/author/<int:author_id>/", views.books_by_author_filter),
path("books/search/", views.search_books),
path("books/price-range/", views.books_price_range),
path("books/available/", views.available_books),
path("books/order-by-date/", views.books_order_by_date),
path("books/top-5/", views.top_five_books),
]