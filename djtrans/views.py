from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"book_list": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "book_detail.html", {"book": book})