from django.db import transaction
from src.api.serializers.author import AuthorInputSerializer,AuthorOutputSerializer
from src.api.models import Author,MetaData
import uuid
from rest_framework import status

class AuthorService:

    @staticmethod
    def createAuthor(data:AuthorInputSerializer)->Author:
        try:
            author=Author(
                user_id=data.user_id,
                name=data.name,
                email=data.email
            )
            return author
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def updateAuthor(data:AuthorInputSerializer)->Author:
        try:
            author=Author.objects.get(user_id=data.user_id)
            author.name=data.name
            author.email=data.email
            return author
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def createAuthorMeta(data:AuthorInputSerializer,author:Author)->MetaData:
        try:
            author_meta=MetaData(
                meta_id=uuid.uuid3(namespace=uuid.NAMESPACE_DNS,name=author.user_id),
                author=author,
                address=data.author_meta.address,
                age=data.author_meta.age
            )
            return author_meta
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def updateAuthorMeta(data:AuthorInputSerializer)->MetaData:
        try:
            if not data.author_meta.get('meta_id'):
                raise Exception("while updating you must pass meta_id...")
            if not MetaData.objects.filter(meta_id=data.author_meta.meta_id).exists():
                raise Exception("wrong meta_id!")
            author_meta=MetaData.objects.get(meta_id=data.author_meta.meta_id)
            author_meta.address=data.author_meta.address
            author_meta.age=data.author_meta.age
            return author_meta
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    @transaction.atomic
    def create(data:dict)->tuple:
        try:
            """
            Schema should be like,
            {
                "user_id": "sanu555",
                "name": "Santanu Jana",
                "email": "SANU@GMAIL.COM",
                "author_meta": {
                    "address": "Muragacha",
                    "age": 21
                }
            }
            """
            serailizer=AuthorInputSerializer(data=data,creation=True)
            if serailizer.is_valid():
                author=AuthorService.createAuthor(data=serailizer.validated_data)
                author_meta=AuthorService.createAuthorMeta(data=serailizer.validated_data,author=author)
                author.save()
                author_meta.save()
                return (
                    {"message":"created!",
                     "author":AuthorOutputSerializer(instance=author).data},
                     status.HTTP_201_CREATED
                )
            else:
                return (
                    {"message":serailizer.errors},
                    status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            raise Exception(str(e))
    

    @staticmethod
    @transaction.atomic
    def update(data:dict)->tuple:
        try:
            """
            Schema should be like,
            {
                "user_id": "sanu555",
                "name": "Santanu Jana",
                "email": "SANU@GMAIL.COM",
                "author_meta": {
                    "meta_id": "812baf55-04fb-3be6-b940-8fe33eb60db9",
                    "address": "Muragacha",
                    "age": 21
                }
            }
            """
            serailizer=AuthorInputSerializer(data=data,creation=False)
            if serailizer.is_valid():
                author=AuthorService.updateAuthor(data=serailizer.validated_data)
                author_meta=AuthorService.updateAuthorMeta(data=serailizer.validated_data)
                author.save()
                author_meta.save()
                return (
                    {"message":"updated!",
                     "author":AuthorOutputSerializer(instance=author).data},
                     status.HTTP_202_ACCEPTED
                )
            else:
                return (
                    {"message":serailizer.errors},
                    status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def delete(author_id:str)->tuple:
        try:
            if not Author.objects.filter(user_id=author_id).exists():
                raise Exception("author does not exists!")
            Author.objects.get(user_id=author_id).delete()
            return (
                {"message":"deleted!"},
                status.HTTP_202_ACCEPTED
            )
        except Exception as e:
            raise Exception(str(e))