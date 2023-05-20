from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Product, Category, Profile, Order, OrderEntry


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    pass


class OrderEntryInline(admin.TabularInline):
    model = OrderEntry
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderEntryInline]


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
