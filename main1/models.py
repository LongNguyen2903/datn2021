
# Create your models here.
from django.db import models
import random
import string
from datetime import date
# Create your models here.

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return result_str
    
class CustomerUser(models.Model):
    U_id = models.IntegerField(primary_key=True, default=get_random_string(5))
    U_name = models.CharField(max_length=200)
    U_gmail = models.CharField(max_length=200)
    U_password = models.CharField(max_length=200)
    U_repeat_password = models.CharField(max_length=200, default='')
    U_phone = models.CharField(max_length=20)
    U_address = models.CharField(max_length=255)
   
class Cart(models.Model):
    Cart_user_id = models.IntegerField(default=0)
    Cart_price = models.IntegerField(default=0)
    Cart_pr_id = models.IntegerField(default=0)
    Cart_pr_name = models.CharField(max_length=255, default="")
    Cart_quantity = models.IntegerField(default=0)
    Cart_product_image = models.CharField(max_length=255, default="")
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)

class FeedbackModel(models.Model):
    Fb_title = models.CharField(max_length=255,default="")
    Fb_content = models.TextField(max_length=255,default="")
    Fb_user_id = models.IntegerField(default=0)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)


class Category_products(models.Model):
    Cpr_name = models.CharField(max_length=255, default=0)
    Cpr_active = models.BooleanField(default=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now=True)


class Product(models.Model):
    Pr_id = models.AutoField(primary_key=True)
    Pr_name = models.CharField(max_length=255)
    Pr_sale = models.BooleanField(default=True)
    Pr_price_sale = models.IntegerField(default=0)
    Pr_price = models.IntegerField(default=0)
    Pr_description = models.TextField(default=0)
    Pr_quantity = models.IntegerField(default=0)
    Pr_category = models.ForeignKey(Category_products, on_delete=models.CASCADE)
    Pr_buy = models.IntegerField(default=0)
    Pr_image = models.CharField(max_length=255,default=0)
    Pr_like = models.IntegerField(default=0)
    Pr_active = models.BooleanField(default=True)
    CreateAt = models.DateTimeField(auto_now_add=True)
    UpdateAt = models.DateTimeField(auto_now= False)


class Order(models.Model):
    Od_id = models.IntegerField(default=0)
    Od_user_id = models.IntegerField(default=0)
    Od_pr_id = models.IntegerField(default=0)
    Od_quantity = models.IntegerField(default=0)
    Od_price = models.IntegerField(default=0)
    Od_status = models.IntegerField(default=0)
    Od_name = models.CharField(max_length=50, default="")
    Od_address = models.CharField(max_length=50, default="")
    Od_phone = models.CharField(max_length=20, default="")
    UpdateAt = models.DateField(default=date.today)

class Transactions(models.Model):
    Tst_email = models.CharField(max_length=50,default=0)
    Tst_name = models.CharField(max_length=50,default=0)
    Tst_address = models.CharField(max_length=50,default=0)
    Tst_phone = models.CharField(max_length=20, default=0)
    Tst_total = models.IntegerField(default=0)
    Tst_status = models.BooleanField(default=True)
    Tst_user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    Tst_date_buy = models.DateTimeField(default=0) 
    Tst_active = models.BooleanField(default=True)
    

class ProductSold(models.Model):
    name = models.CharField(max_length=50, default='')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    create_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class ProductImport(models.Model):
    name = models.CharField(max_length=50, default='')
    quantity = models.IntegerField(default=0)
    import_price = models.IntegerField(default=0)
    supplier = models.CharField(max_length=50,default='')
    UpdateAt = models.DateField(default=date.today)