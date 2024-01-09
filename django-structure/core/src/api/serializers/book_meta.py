from rest_framework import serializers
from src.api.models import BookMeta

class BookMetaOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookMeta
        fields=(
            'bookemeta_id',
            'price',
            'launch_date'
        )
    
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

class BookMetaInputSerializer(serializers.Serializer):
    bookemeta_id=serializers.CharField(required=False)
    price=serializers.CharField()
    launch_date=serializers.DateTimeField(required=False)
