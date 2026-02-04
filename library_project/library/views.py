from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.db.models import Count
from .models import Book, Loan, Member, Category


# Home page
def home(request):
    return HttpResponse("Welcome to Library System")


# FBV: list all books
def book_list(request):
    books = Book.objects.select_related('author').prefetch_related('categories')
    return render(request, 'library/book_list.html', {'books': books})


# CBV: create loan
class CreateLoanView(View):
    def post(self, request, book_id):
        member_id = request.POST.get('member_id')

        book = get_object_or_404(Book, id=book_id)
        member = get_object_or_404(Member, id=member_id)

        loan = Loan.objects.create(book=book, member=member)

        return JsonResponse({
            'message': 'Loan created successfully',
            'loan_id': loan.id
        })


# 1️⃣ Books that have never been loaned
def books_never_loaned_view(request):
    books = Book.objects.filter(loan__isnull=True)
    return render(request, 'library/book_list.html', {'books': books})


# 2️⃣ Books in Science category written by Isaac Newton
def science_newton_books_view(request):
    books = Book.objects.filter(
        categories__name="Science",
        author__name="Isaac Newton"
    )
    return render(request, 'library/book_list.html', {'books': books})


# 3️⃣ Top 3 members with most loans
def top_members_view(request):
    members = Member.objects.annotate(
        loan_count=Count('loan')
    ).order_by('-loan_count')[:3]

    return render(request, 'library/top_members.html', {'members': members})


# 4️⃣ Count books in each category
def books_per_category_view(request):
    categories = Category.objects.annotate(
        book_count=Count('book')
    )
    return render(request, 'library/books_per_category.html', {'categories': categories})


# Bonus: Return books as JSON
def book_list_json(request):
    books = Book.objects.all()

    data = []
    for book in books:
        data.append({
            'title': book.title,
            'author': book.author.name,
            'categories': [cat.name for cat in book.categories.all()],
            'available_copies': book.available_copies,
            'isbn': book.isbn,
        })

    return JsonResponse({'books': data})
