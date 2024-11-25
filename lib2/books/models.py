from django.db import models

# Create your models here.
class Book(models.Model):
    #table definition
    #attributes or field
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    pages=models.IntegerField()
    price=models.IntegerField()
    language=models.CharField(max_length=30)
    cover=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")

    def __str__(self):
        return self.title