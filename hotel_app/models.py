from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50, unique=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Meta:
    ordering = ["author"]
