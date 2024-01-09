from src.api.models import Book,BookMeta,Author
from src.api.serializers.book import BookInputSerializer,BookOutputSerializer
from rest_framework import status
import uuid
from django.db import transaction
from django.utils import timezone


class BookService:

    @staticmethod
    def createBook(data:BookInputSerializer)->Book:
        try:
            book=Book(
                book_id=uuid.uuid1(),
                author=Author.objects.get(user_id=data.author),
                book_name=data.book_name
            )
            return book
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def updateBook(data:BookInputSerializer)->Book:
        try:
            book=Book.objects.get(book_id=data.book_id)
            book.book_name=data.book_name
            return book
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def updateBookMeta(data:BookInputSerializer)->BookMeta:
        try:
            if not data.book_meta.get('bookemeta_id'):
                raise Exception("while updating you must pass bookmeta_id...")
            if not BookMeta.objects.filter(bookemeta_id=data.book_meta.bookemeta_id).exists():
                raise Exception("wrong bookemeta_id!")
            book_meta=BookMeta.objects.get(bookemeta_id=data.book_meta.bookemeta_id)
            book_meta.price=data.book_meta.price
            return book_meta
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def createBookMeta(data:BookInputSerializer,book:Book)->BookMeta:
        try:
            book_meta=BookMeta(
                bookemeta_id=uuid.uuid1(),
                book=book,
                price=data.book_meta.price,
                launch_date=timezone.now()
            )
            return book_meta
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    @transaction.atomic
    def create(data:dict)->tuple:
        try:
            """
            Schema like,
            {
                "books": [
                    {
                        "author": "uts123",
                        "book_name": "VVVV",
                        "book_meta": {
                            "price": "88"
                        }
                    },
                    {
                        "author": "uts123",
                        "book_name": "IOOO",
                        "book_meta": {
                            "price": "74"
                        }
                    }
                ]
        
            }
            """
            serializer=BookInputSerializer(data=data.pop('books'),creation=True,many=True)
            if serializer.is_valid():
                books=[]
                for data in serializer.validated_data:
                    book=BookService.createBook(data=data)
                    book_meta=BookService.createBookMeta(data=data,book=book)
                    book.save()
                    book_meta.save()
                    books.append(book)
                return (
                    {"message":"created!",
                     "book":BookOutputSerializer(instance=books,many=True).data},
                     status.HTTP_201_CREATED
                )
            else:
                return (
                    {"message":serializer.errors},
                    status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    @transaction.atomic
    def update(data:dict)->tuple:
        try:
            """
            Schema like,
                    {
                        "book_id": "e1ec64e2-a658-11ee-93d5-18c04d5465c7",
                        "author": "uts123",
                        "book_name": "IOOO",
                        "book_meta": {
                            "bookemeta_id": "e1ec64e3-a658-11ee-840a-18c04d5465c7",
                            "price": "74",
                            "launch_date": "2023-12-29T20:15:17.276285+05:30"
                        }
                    }
            """
            serializer=BookInputSerializer(data=data,creation=False)
            if serializer.is_valid():
                
                book=BookService.updateBook(data=serializer.validated_data)
                book_meta=BookService.updateBookMeta(data=serializer.validated_data)
                book.save()
                book_meta.save()
                    
                return (
                    {"message":"updated!",
                     "book":BookOutputSerializer(instance=book).data},
                     status.HTTP_202_ACCEPTED
                )
            else:
                return (
                    {"message":serializer.errors},
                    status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def delete(book_id:str)->tuple:
        try:
            if not Book.objects.filter(book_id=book_id).exists():
                raise Exception("book does not exists!")
            Book.objects.get(book_id=book_id).delete()
            return (
                {"message":"deleted!"},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(str(e))