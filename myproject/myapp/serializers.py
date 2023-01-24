from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description')

    # Custom validation function for the 'name' field
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    # Custom validation function for the entire serializer 
    def validate(self, data):
        name = data.get('name')
        description = data.get('description')

        if name == description:
            raise serializers.ValidationError("Description and name cannot be the same.")
        return data
