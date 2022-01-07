from django.contrib import admin
from .models import CustomerUser, Cart, Category_products, FeedbackModel, Product, Order, Transactions, ProductSold, \
    ProductImport
from django.conf.urls import url
from django.template.response import TemplateResponse

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Cart)
admin.site.register(Category_products)
admin.site.register(FeedbackModel)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Transactions)
admin.site.register(ProductSold)
admin.site.register(ProductImport)

