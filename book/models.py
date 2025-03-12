from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

