from book.models import Book
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from book.api.serializers import BookSerializer
from rest_framework import permissions
from book.api.permissions import isAdminUserOrReadOnly

class books_list_api_view(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [isAdminUserOrReadOnly]

class books_details_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [isAdminUserOrReadOnly]


"""
class books_list_api_view(ListModelMixin, CreateModelMixin,GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""






