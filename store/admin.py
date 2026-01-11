from django.contrib import admin
from .models import Category, Product, Size, ProductInventory, Cart, CartItem

# 1. Configuración Básica
admin.site.register(Category)
admin.site.register(Size)

# 2. Configuración de INVENTARIO (Para verlo dentro del producto)
class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1

# 3. Configuración de PRODUCTOS
# (El @admin.register reemplaza al admin.site.register, es lo mismo pero mejor)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active')
    inlines = [ProductInventoryInline] # Esto te muestra el stock ahí mismo

# 4. Configuración del CARRITO (¡ACÁ ESTÁ!)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at') # Muestra usuario y fecha

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'created_at')
