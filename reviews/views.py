from django.shortcuts import render, get_object_or_404

from reviews.models import Book, Review
from reviews.utils import average_rating


def index(request):
    return render(request, "base.html")


def show_book(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        number_of_reviews = len(reviews)
    else:
        book_rating = None
        number_of_reviews = 0
    context = {
        'book': book,
        'reviews': reviews,
        'book_rating': book_rating,
        'number_of_reviews': number_of_reviews
    }
    return render(request, "reviews/show_book.html", context)


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
        context = {
            'book_list': book_list
        }
    return render(request, "reviews/book_list.html", context)


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "reviews/search-results.html", {"search_text": search_text})
