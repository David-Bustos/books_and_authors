from django.shortcuts import render, redirect
from .models import *

### BOOKS ###
def addBook(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'addBook.html', context)

def newBook(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        return redirect('/')

def viewBook(request, number):
    request.session['book_id'] = number
    context = {
        'book': Book.objects.get(id = number),
        'authors': Author.objects.exclude(books = number),
    }
    return render(request, 'viewBook.html', context) 

def Book_add_Author(request):
    author_add = Author.objects.get(id = request.POST['author'])
    book_id = request.session['book_id']
    if request.method == "POST":
        Book.objects.get(id=book_id).authors.add(author_add)
        return redirect(f'/books/{book_id}') 

### AUTHORS ###
def addAuthor(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'addAuthor.html', context)

def newAuthor(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['notes'])
        return redirect('/authors')

def viewAuthor(request, number):
    request.session['author_id'] = number
    context = {
        'author': Author.objects.get(id = number),
        'books': Book.objects.exclude(authors = number),
    }
    return render(request, 'viewAuthor.html', context)

def Author_add_Book(request):
    book_add = Book.objects.get(id = request.POST['book'])
    author_id = request.session['author_id']
    if request.method == "POST":
        Author.objects.get(id=author_id).books.add(book_add)
        return redirect(f'/authors/{author_id}') 