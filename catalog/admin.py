from django.contrib import admin

# Register your models here.
from .models import Genre, Book, BookCopy, Author
admin.site.register(Genre)


class BooksInstanceInline(admin.TabularInline):
    model = BookCopy
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
admin.site.register(Book, BookAdmin)


class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    ) 
admin.site.register(BookCopy, BookCopyAdmin)

class BooksInline(admin.StackedInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'date_of_birth')
    fields = ['lastname', 'firstname', ('date_of_birth')]
    inlines = [BooksInline]
admin.site.register(Author, AuthorAdmin)