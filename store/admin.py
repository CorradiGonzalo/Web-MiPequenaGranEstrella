from django.contrib import admin
from .models import Category, Product, Size, ProductInventory, Cart, CartItem

# --- CONFIGURACIÓN BÁSICA ---
admin.site.register(Category)
admin.site.register(Size)

# --- PRODUCTOS (Con inventario visible) ---
class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active')
    inlines = [ProductInventoryInline] # Esto te deja ver el stock dentro del producto

# --- CARRITO DE COMPRAS (Nuevo) ---
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'created_at')
