from django.contrib import admin
from crm_admin import models


# Register your models here.


class Seller(admin.ModelAdmin):
    list_display = ('id', 'sell_name',
                    'seller_wechat',
                    'seller_qq',
                    'seller_phone_number',
                    'seller_create_time',
                    'seller_update_time'
                    )


class Product(admin.ModelAdmin):
    list_display = ('id', 'product_name',
                    'product_country',
                    'product_keywords',
                    'product_sold_by',
                    'product_asin',
                    'product_link',
                    'product_num_per_day',
                    'product_num_total',
                    'product_create_time',
                    'product_update_time',
                    'product_seller'
                    )


class Buyer(admin.ModelAdmin):
    list_display = ('id', 'buyer_name',
                    'buyer_country',
                    'buyer_paypal',
                    'buyer_profile',
                    'buyer_agent',
                    'buyer_create_time',
                    'buyer_update_time')


class Order(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'product_id', 'buyer_id', 'order_create_time', 'order_update_time')


class Agent(admin.ModelAdmin):
    list_display = ('id', 'agent_name', 'agent_create_time', 'agent_update_time')


class Country(admin.ModelAdmin):
    list_display = ('id', 'country_name')


admin.site.register(models.Seller, Seller)
admin.site.register(models.Product, Product)
admin.site.register(models.Buyer, Buyer)
admin.site.register(models.Order, Order)
admin.site.register(models.Agent, Agent)
admin.site.register(models.Country, Country)
