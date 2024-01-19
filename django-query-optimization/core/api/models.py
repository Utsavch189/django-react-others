from django.db import models

class Author(models.Model):
    author_id= models.CharField(max_length=100,primary_key=True,default="")
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    book_id= models.CharField(max_length=100,primary_key=True,default="")
    title = models.CharField(max_length=200,null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="book_set")
    publication_date = models.DateField()

    def __str__(self) -> str:
        return self.title