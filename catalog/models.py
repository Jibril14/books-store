from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the book genre(e.g Drama, Fiction)')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,  help_text='We only accept books from these authors')
    summary = models.TextField(max_length=600, help_text='Enter a brief description')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    rating = models.IntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    book_cover = models.CharField(
        max_length=500,
        help_text='Enter image link',
        blank=True,
        default="https://res.cloudinary.com/webmonc/image/upload/v1667726415/portfolio/book-store/bookshelv_lhhpy2.jpg")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    # For admin
    def display_genre(self):
        return ',  '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'First 3 Genre'

   

import uuid
class BookCopy(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique id of this book')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, help_text='Pls select a book to store')
    imprint = models.CharField(max_length=200,  help_text='e.g (First Edition Vista Printing Press)' )
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True ,)
    
    Book_Status = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reversed'),
    )

    status = models.CharField(
        choices=Book_Status,
        max_length=1,
        blank=True,
        default='a',
        help_text='Book status' 
        )

    class Meta:
        ordering = ['due_back']

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f'{self.id} ({self.book.title}) by {self.book.author}'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.book.id)])

        
class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['lastname', 'firstname']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.lastname}, {self.firstname}'    