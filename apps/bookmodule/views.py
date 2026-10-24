from django.http import Http404, HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1), content_type="text/plain")


def invalid_index2(request, val1):
    return HttpResponse(
        "error, expected val1 to be integer",
        status=400,
        content_type="text/plain",
    )


def viewbook(request, bookId):
    book1 = {
        "id": 123,
        "title": "Continuous Delivery",
        "author": "J. Humble and D. Farley",
    }
    book2 = {
        "id": 456,
        "title": "Secrets of Reverse Engineering",
        "author": "E. Eilam",
    }

    targetBook = None
    if book1["id"] == bookId:
        targetBook = book1
    if book2["id"] == bookId:
        targetBook = book2
    if targetBook is None:
        raise Http404("Book not found")

    return render(request, "bookmodule/show.html", {"book": targetBook})
