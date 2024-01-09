from rest_framework import serializers
from src.api.models import MetaData

class AuthorMetaOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=MetaData
        fields=(
            'meta_id',
            'address',
            'age'
        )
    
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)


class AuthorInputMetaSerializer(serializers.Serializer):

    meta_id=serializers.CharField(required=False) # only use while updating.. Because while create author and it's meta data meta_id is system generated so user will not pass meta_id
    address=serializers.CharField()
    age=serializers.IntegerField()

    def validate_age(self, age):
        if age<18:
            raise serializers.ValidationError("age should be greater than 18.")
        return age
