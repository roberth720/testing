from django.contrib import admin
from . models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image')
    
    list_display_links = ('id','name', 'price')

    #list_filter = ('nome', 'sobrenome')

    list_per_page = 10

    search_fields = ('name', 'price')

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippindAddress)
admin.site.register(BannerProduct)
admin.site.register(Perfume_search)
