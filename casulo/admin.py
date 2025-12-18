from django.contrib import admin
from .models import Mensagem, Service, ServiceCategory

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    ordering = ('-data_envio',)
    
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "slug")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "icon", "order", "is_active")
    list_filter = ("category", "is_active", "icon")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")
