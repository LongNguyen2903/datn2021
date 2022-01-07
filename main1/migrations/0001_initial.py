# Generated by Django 2.2 on 2021-11-14 13:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_user_id', models.IntegerField(default=0)),
                ('Cart_price', models.IntegerField(default=0)),
                ('Cart_pr_id', models.IntegerField(default=0)),
                ('Cart_pr_name', models.CharField(default='', max_length=255)),
                ('Cart_quantity', models.IntegerField(default=0)),
                ('Cart_product_image', models.CharField(default='', max_length=255)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cpr_name', models.CharField(default=0, max_length=255)),
                ('Cpr_active', models.BooleanField(default=True)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('U_id', models.IntegerField(default='15794', primary_key=True, serialize=False)),
                ('U_name', models.CharField(max_length=200)),
                ('U_gmail', models.CharField(max_length=200)),
                ('U_password', models.CharField(max_length=200)),
                ('U_repeat_password', models.CharField(default='', max_length=200)),
                ('U_phone', models.CharField(max_length=20)),
                ('U_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fb_title', models.CharField(default=0, max_length=255)),
                ('Fb_content', models.TextField(default=0)),
                ('Fb_user_id', models.IntegerField(default=0)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Od_id', models.IntegerField(default=0)),
                ('Od_user_id', models.IntegerField(default=0)),
                ('Od_pr_id', models.IntegerField(default=0)),
                ('Od_quantity', models.IntegerField(default=0)),
                ('Od_price', models.IntegerField(default=0)),
                ('Od_status', models.IntegerField(default=0)),
                ('Od_name', models.CharField(default='', max_length=50)),
                ('Od_address', models.CharField(default='', max_length=50)),
                ('Od_phone', models.CharField(default='', max_length=20)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('create_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tst_email', models.CharField(default=0, max_length=50)),
                ('Tst_name', models.CharField(default=0, max_length=50)),
                ('Tst_address', models.CharField(default=0, max_length=50)),
                ('Tst_phone', models.CharField(default=0, max_length=20)),
                ('Tst_total', models.IntegerField(default=0)),
                ('Tst_status', models.BooleanField(default=True)),
                ('Tst_date_buy', models.DateTimeField(default=0)),
                ('Tst_active', models.BooleanField(default=True)),
                ('Tst_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main1.CustomerUser')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Pr_id', models.AutoField(primary_key=True, serialize=False)),
                ('Pr_name', models.CharField(max_length=255)),
                ('Pr_sale', models.BooleanField(default=True)),
                ('Pr_price_sale', models.IntegerField(default=0)),
                ('Pr_price', models.IntegerField(default=0)),
                ('Pr_description', models.TextField(default=0)),
                ('Pr_quantity', models.IntegerField(default=0)),
                ('Pr_buy', models.IntegerField(default=0)),
                ('Pr_image', models.CharField(default=0, max_length=255)),
                ('Pr_like', models.IntegerField(default=0)),
                ('Pr_active', models.BooleanField(default=True)),
                ('CreateAt', models.DateTimeField(auto_now_add=True)),
                ('UpdateAt', models.DateTimeField()),
                ('Pr_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main1.Category_products')),
            ],
        ),
    ]