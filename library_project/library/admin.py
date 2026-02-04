from django.contrib import admin
from .models import Book, Author, Category, Member, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available_copies')
    list_filter = ('author', 'categories', 'available_copies')
    search_fields = ('title', 'isbn')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Member)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'loan_date', 'return_date', 'overdue_status')
    list_filter = ('book', 'member', 'loan_date', 'return_date')

    def overdue_status(self, obj):
        return obj.is_overdue()
    overdue_status.boolean = True
    overdue_status.short_description = "Overdue?"
