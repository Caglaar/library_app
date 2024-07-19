from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    review = models.TextField(blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(
        validators= [MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f'Book Name: {self.book.title}  Reviewer: {self.reviewer.username}'
    