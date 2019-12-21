from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('loan-books', views.LoanedBooksByUserListView.as_view(), name='loan-books'),
    path('book/<uuid:pk>/borrow/', views.BorrowABook, name='borrow-book'),
    path('registration', views.UserRegistrationView, name='user-registration'),
    path('book-create', views.BookCopyCreateView.as_view(), name='book-create'),
]