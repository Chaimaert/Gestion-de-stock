from django.urls import path
from .views import (CategoryListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDetailAPIView, CategoryDestroyAPIView,
                    BrandCreateAPIView, BrandDetailAPIView, BrandDestroyAPIView, BrandListAPIView, BrandUpdateAPIView,
                    ProductListAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductDetailAPIView, ProductCreateAPIView,
                    SupplierListAPIView, SupplierCreateAPIView, SupplierDetailAPIView, SupplierDestroyAPIView, SupplierUpdateAPIView,
                    CustomerListAPIView, CustomerCreateAPIView, CustomerDetailAPIView, CustomerUpdateAPIView, CustomerDestroyAPIView,
                    OrderListAPIView, OrderCreateAPIView, OrderDestroyAPIView, OrderDetailAPIView, OrderUpdateAPIView,
                    DeliveryManListAPIView, DeliveryManCreateAPIView, DeliveryManDetailAPIView, DeliveryManUpdateAPIView, DeliveryManDestroyAPIView,
                    StockListAPIView, StockCreateAPIView, StockDetailAPIView, StockUpdateAPIView, StockDestroyAPIView,
                    FactureListAPIView, FactureCreateAPIView, FactureDetailAPIView, FactureUpdateAPIView, FactureDestroyAPIView)


urlpatterns = [
    #Category:
    path('Category/', CategoryListAPIView.as_view(), name='list'),
    path('Category/create', CategoryCreateAPIView.as_view(), name='create'),
    path('Category/<pk>/edit', CategoryUpdateAPIView.as_view(), name='update'),
    path('Category/<pk>/', CategoryDetailAPIView.as_view(), name='update'),
    path('Category/<pk>/delete', CategoryDestroyAPIView.as_view(), name='delete'),
    #Brand:
    path('Brand/', BrandListAPIView.as_view(), name='list'),
    path('Brand/create', BrandCreateAPIView.as_view(), name='create'),
    path('Brand/<pk>/edit', BrandUpdateAPIView.as_view(), name='update'),
    path('Brand/<pk>/', BrandDetailAPIView.as_view(), name='update'),
    path('Brand/<pk>/delete', BrandDestroyAPIView.as_view(), name='delete'),
    #Product:
    path('Product/', ProductListAPIView.as_view(), name='list'),
    path('Product/create', ProductCreateAPIView.as_view(), name='create'),
    path('Product/<pk>/edit', ProductUpdateAPIView.as_view(), name='update'),
    path('Product/<pk>/', ProductDetailAPIView.as_view(), name='update'),
    path('Product/<pk>/delete', ProductDestroyAPIView.as_view(), name='delete'),
    #Supplier:
    path('Supplier/', SupplierListAPIView.as_view(), name='list'),
    path('Supplier/create', SupplierCreateAPIView.as_view(), name='create'),
    path('Supplier/<pk>/edit', SupplierUpdateAPIView.as_view(), name='update'),
    path('Supplier/<pk>/', SupplierDetailAPIView.as_view(), name='update'),
    path('Supplier/<pk>/delete', SupplierDestroyAPIView.as_view(), name='delete'),
    #Customer:
    path('Customer/', CustomerListAPIView.as_view(), name='list'),
    path('Customer/create', CustomerCreateAPIView.as_view(), name='create'),
    path('Customer/<pk>/edit', CustomerUpdateAPIView.as_view(), name='update'),
    path('Customer/<pk>/', CustomerDetailAPIView.as_view(), name='update'),
    path('Customer/<pk>/delete', CustomerDestroyAPIView.as_view(), name='delete'),
    #Order:
    path('Order/', OrderListAPIView.as_view(), name='list'),
    path('Order/create', OrderCreateAPIView.as_view(), name='create'),
    path('Order/<pk>/edit', OrderUpdateAPIView.as_view(), name='update'),
    path('Order/<pk>/', OrderDetailAPIView.as_view(), name='update'),
    path('Order/<pk>/delete', OrderDestroyAPIView.as_view(), name='delete'),
    #DeliveryMan:
    path('DeliveryMan/', DeliveryManListAPIView.as_view(), name='list'),
    path('DeliveryMan/create', DeliveryManCreateAPIView.as_view(), name='create'),
    path('DeliveryMan/<pk>/edit', DeliveryManUpdateAPIView.as_view(), name='update'),
    path('DeliveryMan/<pk>/', DeliveryManDetailAPIView.as_view(), name='update'),
    path('DeliveryMan/<pk>/delete', DeliveryManDestroyAPIView.as_view(), name='delete'),
    #Stock:
    path('Stock/', StockListAPIView.as_view(), name='list'),
    path('Stock/create', StockCreateAPIView.as_view(), name='create'),
    path('Stock/<pk>/edit', StockUpdateAPIView.as_view(), name='update'),
    path('Stock/<pk>/', StockDetailAPIView.as_view(), name='update'),
    path('Stock/<pk>/delete', StockDestroyAPIView.as_view(), name='delete'),
    #Facture:
    path('Facture/', FactureListAPIView.as_view(), name='list'),
    path('Facture/create', FactureCreateAPIView.as_view(), name='create'),
    path('Facture/<pk>/edit', FactureUpdateAPIView.as_view(), name='update'),
    path('Facture/<pk>/', FactureDetailAPIView.as_view(), name='update'),
    path('Facture/<pk>/delete', FactureDestroyAPIView.as_view(), name='delete'),
]
