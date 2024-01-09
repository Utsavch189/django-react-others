from collections.abc import Iterable
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from src.api.utils.db_validation import validate_book_name

class Author(models.Model):
    user_id=models.CharField(max_length=100,primary_key=True,default="")
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True,unique=True)

    def __str__(self) -> str:
        return self.name

class MetaData(models.Model):
    meta_id=models.CharField(max_length=100,primary_key=True,default="")
    author=models.OneToOneField(Author,on_delete=models.CASCADE,related_name='author_meta')
    address=models.CharField(max_length=100,blank=True,null=True)
    age=models.IntegerField()

    def __str__(self) -> str:
        return self.author.name


        
class Book(models.Model):
    book_id=models.CharField(max_length=100,primary_key=True,default="")
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    book_name=models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.book_name
    
    
    def save(self,  *args, **kwargs) -> None:
        validate_book_name(self.book_name) # call custom validation...
        return super().save(*args, **kwargs)

class BookMeta(models.Model):
    bookemeta_id=models.CharField(max_length=100,primary_key=True,default="")
    book=models.OneToOneField(Book,on_delete=models.CASCADE,related_name='book_meta')
    price=models.CharField(max_length=100,blank=True,null=True)
    launch_date=models.DateTimeField(default=datetime.now())

    def clean(self) -> None:
        """
        Model Level Validation:

        actives when '.full_clean()' is called before '.save() for a instance'
        """
        if int(self.price)<20:
            raise Exception('price must be above 20!')
    
    def save(self, *args, **kwargs) -> None:
        self.full_clean() # To invoke 'clean()' method...
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.book.book_name


