from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('matricula', 'rfid', 'type', 'is_active', 'is_staff')  # ✅ Mostrar RFID
    list_filter = ('type', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Información Personal', {'fields': ('type', 'rfid')}),  # ✅ Campo RFID aquí
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'password1', 'password2', 'type', 'rfid', 'is_active', 'is_staff')},  # ✅ RFID aquí también
        ),
    )

    search_fields = ('matricula', 'rfid')
    ordering = ('matricula',)

admin.site.register(CustomUser, CustomUserAdmin)
