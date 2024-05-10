from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    publication_year = models.IntegerField()
    isbn = models.TextField()
    author = models.ManyToManyField(Author, null=False, blank=False)
    
    def __str__(self):
        return self.author.name
    
    