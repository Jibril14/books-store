from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView, UpdateView
from .models import Book, Author, BookCopy, Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime,timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import BorrowBookForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.core.paginator import Paginator

def index(request):
    books = Book.objects.all().order_by('title')
    #first_five = books[:7]
    num_books = books.count()
    books_copies =  BookCopy.objects.all()
    books_copies_count = books_copies.count()
    available_copies = books_copies.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books_paginator = paginator.get_page(page)

    context = {
        'books': books_paginator,
        'num_books': num_books,
        'num_instances': books_copies_count,
        'num_instances_available': available_copies,
        'num_authors': num_authors,
        'books_copies': books_copies,
        'books_paginator': books_paginator,
    }
    return render(request, 'catalog/index.html', context=context)


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookCopy
    template_name ='catalog/bookCopies_list_borrowed_by_user.html'

    def get_queryset(self):
        return BookCopy.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@login_required
def BorrowABook(request, pk):
    book_copy = get_object_or_404(BookCopy, pk=pk)

    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
    
        if form.is_valid():
            book_copy.due_back = form.cleaned_data['return_date']
            book_copy.status = 'o'
            book_copy.borrower = User(request.user.id)
            book_copy.save()
          
            return HttpResponseRedirect(reverse('loan-books') )
    else:
        proposed_return_date = datetime.now() + timedelta(weeks=3)
        form = BorrowBookForm(initial={'return_date': proposed_return_date})
        
    context = {
        'form': form,
        'book_copy': book_copy,
    }
    return render(request, 'catalog/borrowabook.html', context)


class BookCopyCreateView(LoginRequiredMixin, CreateView):
    model = BookCopy
    fields = ( 'id', 'book', 'imprint', 'due_back' )
    template_name = 'catalog/book_create.html'
    

def UserRegistrationView(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('login'))
        print(user_form.errors)

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form':user_form} )

