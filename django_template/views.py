from django.shortcuts import render
from .models import BookStore

# Create your views here.
def home_view(request):
    book = BookStore.objects.get(year_published=1958)
    book_author = BookStore.objects.get(book_author="Chinua Achebe")
    all_books = BookStore.objects.all()
    return render(
        request,
        "home.html",
        {
            "book": book, 
            "book_author": book_author,
            "all_books": all_books
            }
    )
     