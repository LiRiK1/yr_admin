from django.contrib import admin
from .models import JuristName, Payment, User
# Register your models here.

@admin.register(JuristName)
class JuristnameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email', 'phone_number')

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'jurist', 'amount', 'currency', 'status', 'date_created', 'date_completed')

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'user_name', 'tg_name', 'user_phone', 'user_mail', 'active', 'user_coin', 'wallet', 'date_register')
