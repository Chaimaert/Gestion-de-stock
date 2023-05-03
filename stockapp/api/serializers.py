from rest_framework.serializers import ModelSerializer
from stockapp.models import Category
""" To list the data from the db"""

class CategorySerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
