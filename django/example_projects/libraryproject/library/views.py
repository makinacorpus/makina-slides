from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from datetime import date
from .models import Book


def recent_books(request):
    today = date.today()
    threshold = today.replace(year=today.year - 1)

    results = Book.objects.filter(published__gt=threshold)

    return render(request, 'library/book_list.html', {
        'results': results
    })


def book_detail(request, book_id):

    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404

    return render(request, 'library/book_detail.html', {'book': book})


def custom_404_view(request):
    return HttpResponseNotFound("Impossible de trouver cette page")
