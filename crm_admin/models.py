from django.db import models


# Create your models here.


class Seller(models.Model):
    sell_name = models.CharField('名称', max_length=16, unique=True)
    seller_wechat = models.CharField('微信', max_length=64, unique=True)
    seller_qq = models.CharField('QQ', max_length=64, unique=True)
    seller_phone_number = models.CharField('手机号码', max_length=64)
    seller_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    seller_update_time = models.DateTimeField('修改时间', auto_now=True)


class Product(models.Model):
    product_name = models.CharField('名称', max_length=64)
    product_country = models.ForeignKey('Country', on_delete=models.PROTECT)
    product_keywords = models.CharField('关键词', max_length=255)
    product_sold_by = models.CharField('店铺名', max_length=64)
    product_asin = models.CharField('Asin', max_length=64)
    product_link = models.CharField('链接', max_length=64)
    product_num_per_day = models.BigIntegerField('每日单数', )
    product_num_total = models.BigIntegerField('总单数', )
    product_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    product_update_time = models.DateTimeField('修改时间', auto_now=True)
    product_seller = models.ForeignKey('Seller', on_delete=models.PROTECT)


class Agent(models.Model):
    agent_name = models.CharField('名称', max_length=64)
    agent_country = models.ManyToManyField('Country')

    agent_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    agent_update_time = models.DateTimeField('修改时间', auto_now=True)


class Buyer(models.Model):
    buyer_name = models.CharField('名称', max_length=64)
    buyer_country = models.CharField('国家', max_length=64)
    buyer_paypal = models.EmailField('Paypal', )
    buyer_profile = models.CharField('亚马逊Profile', max_length=64)
    buyer_agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    buyer_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    buyer_update_time = models.DateTimeField('修改时间', auto_now=True)


class Order(models.Model):
    order_number = models.CharField('订单ID', max_length=64)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    buyer_id = models.ForeignKey('Buyer', on_delete=models.PROTECT)
    order_create_time = models.DateTimeField('创建时间', auto_now_add=True)
    order_update_time = models.DateTimeField('修改时间', auto_now=True)


class Country(models.Model):
    country_name = models.CharField('国家', max_length=16, unique=True)
