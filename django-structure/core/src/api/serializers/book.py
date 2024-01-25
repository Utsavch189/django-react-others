from rest_framework import serializers
from src.api.models import Book,Author
from src.api.serializers.book_meta import BookMetaOutputSerializer,BookMetaInputSerializer
from benedict  import benedict
from utils.exceptions import main

class BookOutputSerializer(serializers.ModelSerializer):
    book_meta=BookMetaOutputSerializer(many=False)
    class Meta:
        model=Book
        fields=(
            'book_id',
            'author',
            'book_name',
            'book_meta'
        )
    
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)


class BookInputSerializer(serializers.Serializer):

    def __init__(self, instance=None, data=...,creation=True, **kwargs):
        self.creation=creation
        super().__init__(instance, data, **kwargs)

    book_id=serializers.CharField(required=False)
    author=serializers.CharField()
    book_name=serializers.CharField()
    book_meta=BookMetaInputSerializer()

    def validate_author(self,value):
        if not Author.objects.filter(user_id=value).exists():
            raise Exception("author does not exists!")
        return value

    def validate_book_id(self,value):
        if not self.creation:
            if not value:
                raise Exception("while updating you must pass book_id...")
            if not Book.objects.filter(book_id=value).exists():
                raise main.NotExists(detail="book doesn't exists",code=400)
        if self.creation:
            if value:
                raise Exception('no need to pass book_id while create!')
        return value
    
    def validate(self, data):
        return benedict(data)