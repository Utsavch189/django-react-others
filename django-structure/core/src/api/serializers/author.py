from rest_framework import serializers
from src.api.models import Author,MetaData
from src.api.serializers.book import BookOutputSerializer
from src.api.serializers.author_meta import AuthorMetaOutputSerializer,AuthorInputMetaSerializer
from benedict import benedict

class AuthorOutputSerializer(serializers.ModelSerializer):
    author_meta=AuthorMetaOutputSerializer(many=False)
    books=BookOutputSerializer(many=True)
    class Meta:
        model=Author
        fields=(
            'user_id',
            'name',
            'email',
            'author_meta',
            'books'
        )
    
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)


class AuthorInputSerializer(serializers.Serializer):

    def __init__(self, instance=None, data=...,creation=True, **kwargs):
        self.creation=creation
        super().__init__(instance, data, **kwargs)

    user_id=serializers.CharField()
    name=serializers.CharField()
    email=serializers.EmailField()
    author_meta=AuthorInputMetaSerializer()
    """
    If we pass author_meta as a list of objects then we must do 'author_meta=AuthorInputMetaSerializer(many=True)'
    """

    def validate_user_id(self,value):
        if self.creation:
            if Author.objects.filter(user_id=value).exists():
                raise serializers.ValidationError("user_id is already exists!")
        else:
            if not Author.objects.filter(user_id=value).exists():
                raise Exception("author does not exists!")
        return value

    def validate_email(self,value):
        """
        Serializer Level Validation.
        
        particular field validation where we must put 'validate_' before the field name as func name,
        authomatically called while 'serializer.is_valid()' is called.
        """
        value=value.upper()
        if self.creation:
            if Author.objects.filter(email=value).exists():
                raise serializers.ValidationError("email is already exists!")
        return value
    
    

    def validate(self, data):
        """
        used to validate whole data, authomatically called while 'serializer.is_valid()' is called.
        """
        return benedict(data)


