from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Customer, Collection, Product, Order, OrderItem


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_product']
    list_display = ('title', 'product_count')
    search_fields = ('title',)

    @admin.display(ordering='products_count')
    def product_count(self, collection):
        url = reverse('admin:store_product_changelist') + \
            '?' + urlencode({'collection__id': str(collection.id)})
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('products'))


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inv'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ('title', 'unit_price', 'inventory_status', 'collection')
    list_editable = ('unit_price',)
    list_filter = ('collection', 'last_update', InventoryFilter)
    list_per_page = 100
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'

    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f'{updated_count} products were updated succesfully.'
        )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership', 'orders')
    list_editable = ('membership',)
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ('first_name__istartswith', 'last_name__istartswith')

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = reverse('admin:store_order_changelist') + \
            '?' + urlencode({'customer__id': str(customer.id)})
        return format_html('<a href="{}">{}</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order'))


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ('product',)
    model = OrderItem
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ('id', 'placed_at', 'customer')


# admin.site.register(Customer)
# admin.site.register(Collection)
# admin.site.register(Product)
