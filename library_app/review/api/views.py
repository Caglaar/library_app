from review.models import Review
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from review.api.serializers import ReviewSerializer
from rest_framework import generics
from book.models import Book
from review.api.permissions import isAdminUserOrReadOnly
from review.api.permissions import isReviewerOrReadOnly


class review_list_api_view(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [isAdminUserOrReadOnly]

class review_details_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [isAdminUserOrReadOnly]


class review_make_api_view(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [isReviewerOrReadOnly]


    def perform_create(self, serializer):
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        serializer.save(reviewer= self.request.user, book = book)

    



"""
class reviews_list_api_view(ListModelMixin, CreateModelMixin,GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return  self.create(request, *args, **kwargs)
"""