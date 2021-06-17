from django.urls import path		 
from . import views

urlpatterns=[ 
    path ('',views.addBook),
    path ('new_book',views.newBook, name = 'new_book'),
    path ('books/<number>',views.viewBook, name = 'view_book'),
    path ('book_add_author',views.Book_add_Author, name = 'baa'),
    path ('authors',views.addAuthor),
    path ('new_author',views.newAuthor, name = 'new_author'),
    path ('authors/<number>',views.viewAuthor, name = 'view_author'),
    path ('author_add_book',views.Author_add_Book, name = 'aab'),
]