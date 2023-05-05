from rest_framework.generics import (ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView)
from stockapp.models import Category
from stockapp.models import Brand
from stockapp.models import Product
from stockapp.models import Supplier
from stockapp.models import Customer
from stockapp.models import Order
from stockapp.models import DeliveryMan
from stockapp.models import Stock
from stockapp.models import Facture

from .serializers import (CategoryListSerialize, CategoryCreateSerialize, CategoryUpdateSerialize,
                          CategoryDetailSerialize, CategoryDestroySerialize,
                          BrandCreateSerialize, BrandDetailSerialize, BrandListSerialize, BrandUpdateSerialize,
                          BrandDestroySerialize,
                          ProductCreateSerialize, ProductDetailSerialize, ProductUpdateSerialize,
                          ProductDestroySerialize, ProductListSerialize,
                          SupplierListSerialize, SupplierCreateSerialize, SupplierDetailSerialize,
                          SupplierUpdateSerialize, SupplierDestroySerialize,
                          CustomerListSerialize, CustomerCreateSerialize, CustomerDetailSerialize,
                          CustomerUpdateSerialize, CustomerDestroySerialize,
                          OrderListSerialize, OrderCreateSerialize, OrderDetailSerialize, OrderUpdateSerialize,
                          OrderDestroySerialize, DeliveryManListSerialize, DeliveryManCreateSerialize,
                          DeliveryManUpdateSerialize, DeliveryManDetailSerialize, DeliveryManDestroySerialize,
                          StockListSerialize, StockCreateSerialize, StockUpdateSerialize, StockDetailSerialize,
                          StockDestroySerialize,
                          FactureListSerialize, FactureCreateSerialize, FactureUpdateSerialize, FactureDetailSerialize,
                          FactureDestroySerialize)
                          
#Category:
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerialize

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerialize

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerialize

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialize

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDestroySerialize
#end of Category:

#Brand :
class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerialize

class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerialize

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerialize

class BrandDetailAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerialize

class BrandDestroyAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDestroySerialize
#end of Brand:

#Product :
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerialize

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerialize

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerialize

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerialize

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDestroySerialize
#end of Product.

#Supplier :
class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierListSerialize

class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierCreateSerialize

class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerialize

class SupplierDetailAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDetailSerialize

class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierDestroySerialize
#end of Supplier.

#Customer :
class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerialize

class CustomerCreateAPIView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerialize

class CustomerUpdateAPIView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerUpdateSerialize

class CustomerDetailAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerialize
class CustomerDestroyAPIView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDestroySerialize

#Order :
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerialize

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerialize

class OrderUpdateAPIView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerialize

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerialize

class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDestroySerialize
#end of Order.

#DeliveryMan :
class DeliveryManListAPIView(ListAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManListSerialize

class DeliveryManCreateAPIView(CreateAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManCreateSerialize

class DeliveryManUpdateAPIView(UpdateAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManUpdateSerialize

class DeliveryManDetailAPIView(RetrieveAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManDetailSerialize

class DeliveryManDestroyAPIView(DestroyAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManDestroySerialize
#end of DeliveryMan.

#Stock:
class StockListAPIView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockListSerialize

class StockCreateAPIView(CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockCreateSerialize

class StockUpdateAPIView(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockUpdateSerialize

class StockDetailAPIView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockDetailSerialize

class StockDestroyAPIView(DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockDestroySerialize
#end of Stock.

#Facture:
class FactureListAPIView(ListAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureListSerialize

class FactureCreateAPIView(CreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureCreateSerialize

class FactureUpdateAPIView(UpdateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureUpdateSerialize

class FactureDetailAPIView(RetrieveAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureDetailSerialize

class FactureDestroyAPIView(DestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureDestroySerialize
#end of Facture.