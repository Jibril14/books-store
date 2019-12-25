# Book Store

A Book management website written using Python/Django.

### Attributes

-   Visitors can view list of Books stored, number of books.
-   Visitors can view details of Books stored, Authors of different books.
-   Visitors can Register, login, reset password
-   Authenticated users can borrow books
-   Authenticated Users can view list of books borrowed
-   Authenticated user can loan a book instance to the Book store catalog
-   Admin can create or delete books, can see book status(onloan, borrower, dueback e.t.c) and update books records

### Model Primer

-   The model include Genre, Book, BookCopy, Author
-   Book connect to author through a ForeignKey
-   BookCopy connect to Book model through a ForeignKey
-   BookCopy also has a borrower field connected to User model throgh a ForeignKey

### View Primer

-   The view render different template to users on request
-   Grant Different permissions for users using decorator @permission_required and LoginRequiredMixin
-   views query the database and Pagination data across several pages

### Project Setup

```bash
  1. git clone https://github.com/jibril14/Bookstore.git
  2. cd book_store
  3. python3 -m venv venv
  4. venv/bin/activate
  5. pip3 install -r requirements.txt
  6. Generate a new secret key
  7. python manage.py makemigrations
  8. python manage.py migrate
  9. python manage.py createsuperuser
  10. python manage.py runserver
```

### Project live demo

https://bookstorre.herokuapp.com/
