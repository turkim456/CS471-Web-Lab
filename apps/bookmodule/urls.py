from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="book-index"),
    path("index2/<int:val1>/", views.index2, name="book-index2"),
    path("index2/<str:val1>/", views.invalid_index2, name="book-index2-invalid"),
    path("<int:bookId>", views.viewbook, name="book-detail"),
]
