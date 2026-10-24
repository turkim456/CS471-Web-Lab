from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1), content_type="text/plain")


def invalid_index2(request, val1):
    return HttpResponse("error, expected val1 to be integer", status=400, content_type="text/plain")
