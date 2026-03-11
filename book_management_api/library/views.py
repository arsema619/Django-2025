import json
from django.http import JsonResponse
from .models import Author, Book, Category


def authors_list(request):
    authors = list(Author.objects.values())
    return JsonResponse(authors, safe=False, status=200)


def author_detail(request, id):
    try:
        author = Author.objects.get(id=id)
        data = {
            "id": author.id,
            "name": author.name,
            "bio": author.bio,
            "date_of_birth": author.date_of_birth
        }
        return JsonResponse(data, status=200)

    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)

    
def create_author(request):
    if request.method == "POST":
        data = json.loads(request.body)

        author = Author.objects.create(
            name=data.get("name"),
            bio=data.get("bio"),
            date_of_birth=data.get("date_of_birth")
        )

        return JsonResponse({"message": "Author created", "id": author.id}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)


def update_author(request, id):
    if request.method == "PUT":
        try:
            author = Author.objects.get(id=id)
            data = json.loads(request.body)

            author.name = data.get("name", author.name)
            author.bio = data.get("bio", author.bio)
            author.date_of_birth = data.get("date_of_birth", author.date_of_birth)

            author.save()

            return JsonResponse({"message": "Author updated"}, status=200)

        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)

from django.db.models import Count

def author_book_count(request):
    authors = Author.objects.annotate(book_count=Count("book"))

    data = []
    for a in authors:
        data.append({
            "id": a.id,
            "name": a.name,
            "book_count": a.book_count
        })

    return JsonResponse(data, safe=False, status=200)


def books_by_author(request, id):
    books = Book.objects.filter(author_id=id).values()
    return JsonResponse(list(books), safe=False, status=200)


def delete_author(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return JsonResponse({"message": "Author deleted"}, status=200)

    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)

def books_list(request):
    books = Book.objects.select_related("author").prefetch_related("categories").values()
    return JsonResponse(list(books), safe=False, status=200)


def book_detail(request, id):
    try:
        book = Book.objects.select_related("author").get(id=id)

        data = {
            "id": book.id,
            "title": book.title,
            "author": book.author.name,
            "published_date": book.published_date,
            "isbn": book.isbn,
            "price": book.price,
            "available": book.available
        }

        return JsonResponse(data, status=200)

    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


def create_book(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if Book.objects.filter(isbn=data.get("isbn")).exists():
            return JsonResponse({"error": "ISBN already exists"}, status=400)

        book = Book.objects.create(
            title=data.get("title"),
            author_id=data.get("author"),
            published_date=data.get("published_date"),
            isbn=data.get("isbn"),
            price=data.get("price"),
            available=data.get("available")
        )

        return JsonResponse({"message": "Book created", "id": book.id}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)


def update_book(request, id):
    if request.method == "PUT":
        try:
            book = Book.objects.get(id=id)
            data = json.loads(request.body)

            book.title = data.get("title", book.title)
            book.price = data.get("price", book.price)
            book.available = data.get("available", book.available)

            book.save()

            return JsonResponse({"message": "Book updated"}, status=200)

        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        
    return JsonResponse({"error": "Invalid request"}, status=400)


def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return JsonResponse({"message": "Book deleted"}, status=200)

    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


def books_by_author_filter(request, author_id):
    books = Book.objects.filter(author_id=author_id).values()
    return JsonResponse(list(books), safe=False, status=200)


def books_price_range(request):
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    books = Book.objects.filter(price__gte=min_price, price__lte=max_price).values()
    return JsonResponse(list(books), safe=False, status=200)

def search_books(request):
    query = request.GET.get("q")

    if query:
        books = Book.objects.filter(title__icontains=query).values()
        return JsonResponse(list(books), safe=False, status=200)

    return JsonResponse({"error": "No search query provided"}, status=400)

def available_books(request):
    books = Book.objects.filter(available=True).values()
    return JsonResponse(list(books), safe=False, status=200)

def books_order_by_date(request):
    books = Book.objects.order_by("published_date").values()
    return JsonResponse(list(books), safe=False, status=200)

def top_five_books(request):
    books = Book.objects.all()[:5].values()
    return JsonResponse(list(books), safe=False, status=200)