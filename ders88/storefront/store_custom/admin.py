from django.contrib import admin
from store.models import Product
from tags.models import TaggedItem
from store.admin import ProductAdmin
from django.contrib.contenttypes.admin import GenericTabularInline

class TagInline(GenericTabularInline):
    model = TaggedItem
    extra = 1
    autocomplete_fields = ['tag']


class CustomeProductAdmin(ProductAdmin):
    inlines = [TagInline]


try:
    admin.site.unregister(Product)
except admin.sites.NotRegistered:
    pass

admin.site.register(Product,CustomeProductAdmin)
