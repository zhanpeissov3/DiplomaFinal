from django.contrib import admin
from .models import Service, Category, Product, UserMessage, UserMessageService


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'icon', 'price', 'content', 'photo', 'publish', 'created', 'updated']
    list_filter = ['created', 'updated', 'price']
    list_editable = ['price', ]
    search_fields = ('title', 'content')

    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'subject', 'message')
    list_display_links = ('phone_number', 'subject')
    search_fields = ('user_name', 'phone_number', 'subject',)


class UserMessageServiceAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'service', 'message')
    list_display_links = ('phone_number', 'service')
    search_fields = ('user_name', 'phone_number', 'service',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(UserMessageService, UserMessageServiceAdmin)