
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('matricula', 'type', 'is_active', 'is_staff')
    list_filter = ('type', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Información Personal', {'fields': ('type',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'password1', 'password2', 'type', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('matricula',)
    ordering = ('matricula',)

admin.site.register(CustomUser, CustomUserAdmin)
