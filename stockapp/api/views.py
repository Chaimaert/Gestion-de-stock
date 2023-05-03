from rest_framework.generics import ListAPIView
from stockapp.models import Category
from .serializers import CategorySerialize
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialize

