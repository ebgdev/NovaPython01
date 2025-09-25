from django.contrib import admin
from . import models

admin.site.register(models.Collection)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status','collection','collection_featured_product']
    list_editable = ['unit_price']
    list_per_page = 20

    # baglantida ilisliyi gosteriyorsak eger iki alt-tire kullaniriz
    list_select_related = ['collection','collection__featured_product']

    @admin.display(ordering='collection__featured_product__title',description='Featued Product')
    def collection_featured_product(self,product):
        if product.collection.featured_product:
            return product.collection.featured_product.title
        return '-'

    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','phone','membership']
    list_editable = ['email','phone','membership']
    list_per_page = 20



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']