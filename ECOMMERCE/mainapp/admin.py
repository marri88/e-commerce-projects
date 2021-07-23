from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_display_links = ("name",)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)