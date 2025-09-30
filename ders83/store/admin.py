from django.contrib import admin , messages
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

class InventoryFilter(admin.SimpleListFilter):
    # this will appear in the filter section heading
    title = 'inventory'

    # after the 'By inventory' heading in parameters section
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt =10)
        
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    prepopulated_fields = {'slug':['title']}
    autocomplete_fields = ['collection']
    list_display = ['title','unit_price','inventory_status','collection','collection_featured_product']
    list_editable = ['unit_price']
    list_filter = ['collection','last_update',InventoryFilter]
    list_per_page = 20

    # baglantida ilisliyi gosteriyorsak eger iki alt-tire kullaniriz
    list_select_related = ['collection','collection__featured_product']

    @admin.action(description='Clear Inventory')
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory=0)

        self.message_user(
            request,
            f'{updated_count} Products successfully get updated.',
            messages.SUCCESS
        )



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
        


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','product_count']
    search_fields = ['title']

    @admin.display(ordering='product_count')
    def product_count(self,collection):
        # 'admin:app_model_page'
        # product/?collection__id = 5
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id':str(collection.id)
               }) 
               )
        return format_html('<a href="{}">{}</a>',url,collection.product_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )





@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','membership']
    list_editable = ['email','phone','membership']
    # i -> incase sensitive
    # case sensitive
    search_fields = ['first_name__istartswith','last_name__istartswith','email','phone']
    list_per_page = 20



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']
    autocomplete_fields = ['customer']