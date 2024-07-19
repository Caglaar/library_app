from rest_framework import serializers
from book.models import Book
from review.api.serializers import ReviewSerializer


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many= True, read_only = True)
    
    class Meta:
        model = Book
        read_only_fields = ['borrower']
        fields = "__all__"

