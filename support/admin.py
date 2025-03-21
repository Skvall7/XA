from django.contrib import admin

from .models import Appeal, Document, SupportUser


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'invoice_id', 'amount', 'sup_id', 'provider_id', 'responsible_id', 'status',
                    'expiration_at', 'source_id', 'documents', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['id', 'order_id', 'invoice_id', 'amount', 'sup_id', 'provider_id', 'responsible_id', 'status']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'created_at', 'updated_at']
    list_filter = []
    search_fields = ['id']


@admin.register(SupportUser)
class SupportUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_account', 'email', 'rating', 'reward', 'created_at', 'updated_at']
    list_filter = []
    search_fields = ['id', 'user_account', 'email', 'rating']
