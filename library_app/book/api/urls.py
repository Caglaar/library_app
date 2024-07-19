from django.urls import path
from book.api import views as api_view


urlpatterns = [
    path('books/', api_view.books_list_api_view.as_view(), name="book-list"),
    path('books/<int:pk>', api_view.books_details_api_view.as_view(), name="book-detail"),
]
