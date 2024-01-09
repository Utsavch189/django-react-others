from django.db import models
from .repository import AuthorRepo

class Author(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,primary_key=True,default="")

    objects=models.Manager()
    repo_objects=AuthorRepo

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField()



    def __str__(self) -> str:
        return self.name + " " + self.author.name
