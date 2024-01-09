from src.api.models import Author
from src.api.serializers.author import AuthorOutputSerializer
from rest_framework import status
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


class AuthorSelector:

    @staticmethod
    def get_all_authors()->tuple:
        try:
            authors=Author.objects.all()
            serialized_data=AuthorOutputSerializer(instance=authors,many=True).data
            return (
                {"authors":serialized_data},
                status.HTTP_200_OK
            )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def get_a_author(author_id:str)->tuple:
        try:
            if not Author.objects.filter(user_id=author_id).exists():
                raise Exception("author_id is inavalid!")
            authors=Author.objects.get(user_id=author_id)
            serialized_data=AuthorOutputSerializer(instance=authors).data
            return (
                {"author":serialized_data},
                status.HTTP_200_OK
            )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def get_paginated_authors(page,page_size):
        try:
            authors=Author.objects.all().order_by('user_id')
            paginator=Paginator(authors,page_size)
            try:
                query=paginator.page(page)
            except PageNotAnInteger:
                query=paginator.page(1)
            except EmptyPage:
                query=paginator.page(paginator.num_pages)
                
            serialized_data=AuthorOutputSerializer(instance=query,many=True).data
            return (
                {"authors":serialized_data},
                status.HTTP_200_OK
            )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def get(query_dict):
        try:
            """
                Use Factory Design Pattern
            """
            if not query_dict:
                return AuthorSelector.get_all_authors()
            elif query_dict.get('author-id'):
                return AuthorSelector.get_a_author(author_id=query_dict.get('author-id'))
            elif query_dict.get('page') and query_dict.get('page-size'):
                return AuthorSelector.get_paginated_authors(page=query_dict.get('page'),page_size=query_dict.get('page-size'))
        except Exception as e:
            raise Exception(str(e))
    

