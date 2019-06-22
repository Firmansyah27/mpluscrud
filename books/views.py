from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books.html',{'books':books})

def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'books-form.html',{'form': form})

def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'books-form.html',{'form': form, 'book':book})

def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'book-delete-confirm.html',{'book': book})
