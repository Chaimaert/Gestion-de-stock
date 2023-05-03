from django.contrib import admin
from .models import Category
from .models import Brand
from .models import Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)