from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone', 'mail', 'registry_date', 'category', 'show')
    list_display_links = ('id', 'name')
    # list_filter = ('id', 'name', 'last_name')
    list_per_page = 10
    search_fields = ('name', 'last_name', 'phone')
    list_editable = ('show', 'phone')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
