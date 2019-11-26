from django.contrib import admin
from .models import Orders, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email',\
                    'address','postal_code','city','paid',
                    'created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline]