from django.shortcuts import render

from reviews.models import Book


def index(request):
    return render(request, "base.html")


def book_list(request):
    list_of_books = Book.objects.all()
    return render(request, "books_list.html", {"list_of_books": list_of_books})


# def book_search(request):
#     search_text = request.GET.get("search", "")
#     return render(request, "reviews/search-results.html", {"search_text": search_text})
