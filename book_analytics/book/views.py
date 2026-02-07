from django.shortcuts import render
from django.db.models import Avg, Count, Max, Sum
from .models import Book, Author
from django.db.models import Sum, Prefetch
from .models import Author, Book


# 1) Basic Queries
def query_results_view(request):
    books_after_2010 = Book.objects.filter(published_year__gt=2010)
    python_books = Book.objects.filter(title__icontains="python")
    usa_authors = Author.objects.filter(country="USA").order_by('name')

    context = {
        'books_after_2010': books_after_2010,
        'python_books': python_books,
        'usa_authors': usa_authors,
    }

    return render(request, 'book/query_results.html', context)


# 2) Avoid N+1 Queries
def books_with_authors(request):
    books = Book.objects.select_related('author')  # efficient join
    return render(request, 'book/books_authors.html', {'books': books})


def authors_with_books(request):
    authors = Author.objects.prefetch_related('book_set')  # change to 'books' if you used related_name
    return render(request, 'book/authors_books.html', {'authors': authors})


# 3) Advanced Filtering
def advanced_filtering_view(request):
    books = Book.objects.filter(price__gt=0, isbn__regex=r'^\d{13}$')

    authors = Author.objects.filter(book_set__price__gt=50).distinct()  # change to books__price if related_name='books'

    return render(request, 'book/query_results.html', {
        'books': books,
        'authors': authors
    })


def aggregation_view(request):
    # h) Average price of all books
    avg_price = Book.objects.aggregate(avg_price=Avg('price'))

    # i) Number of books per author
    authors_with_counts = Author.objects.annotate(book_count=Count('books'))

    # j) Author with the most expensive book
    most_expensive_book = Book.objects.order_by('-price').first()
    most_expensive_author = most_expensive_book.author if most_expensive_book else None

    # k) Author stats (>= 2 books)
    authors_stats = Author.objects.annotate(
        total_books=Count('books'),
        avg_price=Avg('books__price'),
        total_revenue=Sum('books__price')
    ).filter(total_books__gte=2)

    context = {
        'avg_price': avg_price['avg_price'],
        'authors_with_counts': authors_with_counts,
        'most_expensive_author': most_expensive_author,
        'authors_stats': authors_stats,
    }

    return render(request, 'book/query_results.html', context)


def top_authors_view(request):
    top_authors = (
        Author.objects
        .annotate(total_revenue=Sum('books__price'))   # calculate revenue
        .order_by('-total_revenue')[:5]               # top 5 authors
        .prefetch_related(
            Prefetch('books', queryset=Book.objects.only('title'))
        )                                             # fetch book titles efficiently
    )

    return render(request, 'book/top_authors.html', {'top_authors': top_authors})
