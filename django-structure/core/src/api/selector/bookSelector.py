from src.api.models import Book
from src.api.serializers.book import BookOutputSerializer
from rest_framework import status
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from utils.exceptions import main

class BookSelector:

    @staticmethod
    def get_all_books()->tuple:
        books=Book.objects.all()
        serialized_data=BookOutputSerializer(instance=books,many=True).data
        return (
            {"books":serialized_data},
            status.HTTP_200_OK
        )
    
    @staticmethod
    def get_a_book(book_id:str)->tuple:
        if not Book.objects.filter(book_id=book_id).exists():
            #raise Exception("book does not exists!")
            raise main.NotExists(detail="book doesn't exists",code=404)
        books=Book.objects.get(book_id=book_id)
        serialized_data=BookOutputSerializer(instance=books).data
        return (
            {"book":serialized_data},
            status.HTTP_200_OK
        )
    
    @staticmethod
    def get_paginated_books(page,page_size):
        books=Book.objects.all().order_by('book_id')
        paginator=Paginator(books,page_size)
        try:
            query=paginator.page(page)
        except PageNotAnInteger:
            query=paginator.page(1)
        except EmptyPage:
            query=paginator.page(paginator.num_pages)
            
        serialized_data=BookOutputSerializer(instance=query,many=True).data
        return (
            {"books":serialized_data},
            status.HTTP_200_OK
        )

    
    @staticmethod
    def get(query_dict):
        """
            Use Factory Design Pattern
        """
        if not query_dict:
            return BookSelector.get_all_books()
        elif query_dict.get('book-id'):
            return BookSelector.get_a_book(book_id=query_dict.get('book-id'))
        elif query_dict.get('page') and query_dict.get('page-size'):
            return BookSelector.get_paginated_books(page=query_dict.get('page'),page_size=query_dict.get('page-size'))