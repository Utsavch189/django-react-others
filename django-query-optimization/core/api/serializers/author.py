from rest_framework import serializers
from api.models import Author
from api.serializers.book import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):

    book_set = BookSerializer(many=True)    

    class Meta:
        model = Author
        fields = ('author_id','name','book_set')


    