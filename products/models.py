from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100) #name of the book
    edition = models.PositiveIntegerField() #edition number   
    publication_year = models.DateField() #edition number   
    authors = models.CharField(max_length=100)
    def __str__(self):
        return self.description