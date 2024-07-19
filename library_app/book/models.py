from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, default="0000000000000")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    avaible = models.BooleanField(default=True)
    delivery_date = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=255)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.title}  - {self.author}'
