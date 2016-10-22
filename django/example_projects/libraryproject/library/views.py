from django.shortcuts import render
from datetime import date
from .models import Book


def recent_books(request):
    today = date.today()
    threshold = today.replace(year=today.year - 1)

    results = Book.objects.filter(published__gt=threshold)

    return render(request, 'library/book_list.html', {
        'results': results
    })
