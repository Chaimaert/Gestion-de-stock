from rest_framework.serializers import ModelSerializer
from stockapp.models import Category
from stockapp.models import Brand
from stockapp.models import Product
from stockapp.models import Supplier
from stockapp.models import Customer
from stockapp.models import Order
from stockapp.models import DeliveryMan
from stockapp.models import Stock
from stockapp.models import Facture

#Start class Category:

#Category List:
class CategoryListSerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

#Category Create:
class CategoryCreateSerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

#Category Update:
class CategoryUpdateSerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

#Category Detail:
class CategoryDetailSerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]

#Category Delete:
class CategoryDestroySerialize(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
#end class Category.

#Start class Brand:

#Brand List:
class BrandListSerialize(ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture',
        ]

#Brand Create:
class BrandCreateSerialize(ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture',
        ]

#Brand Update:
class BrandUpdateSerialize(ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture',
        ]

#Brand Detail:
class BrandDetailSerialize(ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture',
        ]

#Brand Delete:
class BrandDestroySerialize(ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture',
        ]
#end class Brand.

#Start class Product:

#Product List:
class ProductListSerialize(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'brand',
            'category',
            'quantity',
            'user',
            'picture',
            'alert',
            'Last_Edate',
            'Last_Odate'
        ]

#Product Create:
class ProductCreateSerialize(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'brand',
            'category',
            'quantity',
            'user',
            'picture',
            'alert',
            'Last_Edate',
            'Last_Odate'
        ]

#Product Update:
class ProductUpdateSerialize(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'brand',
            'category',
            'quantity',
            'user',
            'picture',
            'alert',
            'Last_Edate',
            'Last_Odate'
        ]

#Product Detail:
class ProductDetailSerialize(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'brand',
            'category',
            'quantity',
            'user',
            'picture',
            'alert',
            'Last_Edate',
            'Last_Odate'
        ]

#Product Delete:
class ProductDestroySerialize(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'brand',
            'category',
            'quantity',
            'user',
            'picture',
            'alert',
            'Last_Edate',
            'Last_Odate'
        ]
#end class Product.

#Start class Supplier:

#Supplier List:
class SupplierListSerialize(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'phone',
            'company_name',
            'company_address',
            'email',
        ]

#Supplier Create:
class SupplierCreateSerialize(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'phone',
            'company_name',
            'company_address',
            'email',
        ]

#Supplier Update:
class SupplierUpdateSerialize(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'phone',
            'company_name',
            'company_address',
            'email',
        ]

#Supplier Detail:
class SupplierDetailSerialize(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'phone',
            'company_name',
            'company_address',
            'email',
        ]

#Supplier Delete:
class SupplierDestroySerialize(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'phone',
            'company_name',
            'company_address',
            'email',
        ]
#end class Supplier.

#Start class Customer:

#Customer List:
class CustomerListSerialize(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'name',
            'description',
        ]

#Customer Create:
class CustomerCreateSerialize(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'user_name',
            'email',
            'password',
            'phone_num',
            'address',
        ]

#Customer Update:
class CustomerUpdateSerialize(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'user_name',
            'email',
            'password',
            'phone_num',
            'address',
        ]

#Customer Detail:
class CustomerDetailSerialize(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'user_name',
            'email',
            'password',
            'phone_num',
            'address',
        ]

#Customer Delete:
class CustomerDestroySerialize(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'user_name',
            'email',
            'password',
            'phone_num',
            'address',
        ]
#end class Customer.

#Start class Order:

#Order List:
class OrderListSerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'customer',
            'product',
            'price',
            'taxes',
            'discount',
            'date',
            'qte',
        ]

#Order Create:
class OrderCreateSerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'customer',
            'product',
            'price',
            'taxes',
            'discount',
            'date',
            'qte',
        ]

#Order Update:
class OrderUpdateSerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'customer',
            'product',
            'price',
            'taxes',
            'discount',
            'date',
            'qte',
        ]

#Order Detail:
class OrderDetailSerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'customer',
            'product',
            'price',
            'taxes',
            'discount',
            'date',
            'qte',
        ]

#Order Delete:
class OrderDestroySerialize(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'user',
            'customer',
            'price',
            'taxes',
            'discount',
            'date',
            'qte',
        ]
#end class Order.

#Start class DeliveryMan:

#DeliveryMan List:
class DeliveryManListSerialize(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'name',
            'description',
        ]

#DeliveryMan Create:
class DeliveryManCreateSerialize(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'name',
            'description',
            'phone',
            'address',
            'email',
            'password',
            'salary',
            'order',
        ]

#DeliveryMan Update:
class DeliveryManUpdateSerialize(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'name',
            'description',
            'phone',
            'address',
            'email',
            'password',
            'salary',
            'order',
        ]

#DeliveryMan Detail:
class DeliveryManDetailSerialize(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'name',
            'description',
            'phone',
            'address',
            'email',
            'password',
            'salary',
            'order',
        ]

#DeliveryMan Delete:
class DeliveryManDestroySerialize(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'name',
            'description',
            'phone',
            'address',
            'email',
            'password',
            'salary',
            'order',
        ]
#end class DeliveryMan.

#Start class Stock:

#Stock List:
class StockListSerialize(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'type',
            'quantity',
            'update_date',
        ]

#Stock Create:
class StockCreateSerialize(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'type',
            'quantity',
            'update_date',
        ]

#Stock Update:
class StockUpdateSerialize(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'type',
            'quantity',
            'update_date',
        ]

#Stock Detail:
class StockDetailSerialize(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'type',
            'quantity',
            'update_date',
        ]

#Stock Delete:
class StockDestroySerialize(ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'type',
            'quantity',
            'update_date',
        ]
#end class Stock.

#Start class Facture:

#v List:
class FactureListSerialize(ModelSerializer):
    class Meta:
        model = Facture
        fields = [
            'date',
            'order',
            'product',
            'delivery_man',
        ]

#Facture Create:
class FactureCreateSerialize(ModelSerializer):
    class Meta:
        model = Facture
        fields = [
            'date',
            'order',
            'product',
            'delivery_man',
        ]

#Facture Update:
class FactureUpdateSerialize(ModelSerializer):
    class Meta:
        model = Facture
        fields = [
            'date',
            'order',
            'product',
            'delivery_man',
        ]

#Facture Detail:
class FactureDetailSerialize(ModelSerializer):
    class Meta:
        model = Facture
        fields = [
            'date',
            'order',
            'product',
            'delivery_man',
        ]

#Facture Delete:
class FactureDestroySerialize(ModelSerializer):
    class Meta:
        model = Facture
        fields = [
            'date',
            'order',
            'product',
            'delivery_man',
        ]
#end class Facture.

