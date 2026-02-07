from django.urls import path
from .views import (
    query_results_view,
    books_with_authors,
    authors_with_books,
    advanced_filtering_view,
    aggregation_view,
    top_authors_view,   # ✅ ADD THIS
)

urlpatterns = [
    path('queries/', query_results_view, name='query_results'),
    path('books_authors/', books_with_authors, name='books_authors'),
    path('authors_books/', authors_with_books, name='authors_books'),
    path('advanced/', advanced_filtering_view, name='advanced_filtering'),
    path('aggregation/', aggregation_view, name='aggregation'),
    
    path('top-authors/', top_authors_view, name='top_authors'),  
]
