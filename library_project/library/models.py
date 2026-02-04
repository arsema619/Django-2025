from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)  # ✅ added

    def is_overdue(self):
        if self.return_date:
            return self.return_date < timezone.now().date()
        return False

    def __str__(self):
        return f"{self.book.title} -> {self.member.name}"

