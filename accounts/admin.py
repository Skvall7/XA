from django.contrib import admin

from .models import UserAccounts, TelegramBotSettings


@admin.register(UserAccounts)
class UserAccountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'patronymic_name', 'login', 'birthday', 'is_active',
                    'is_confirmed', 'in_consideration', 'is_staff']
    list_filter = ['is_active', 'is_confirmed', 'in_consideration', 'is_staff']
    search_fields = ['id', 'first_name', 'last_name', 'patronymic_name', 'login']


@admin.register(TelegramBotSettings)
class TelegramBotSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'notification_type', 'bot_token', 'created_at', 'updated_at']
    list_filter = ['notification_type', 'bot_token']
    search_fields = ['id', 'notification_type', 'bot_token']
