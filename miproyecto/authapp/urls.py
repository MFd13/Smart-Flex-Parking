from django.contrib import admin
from django.urls import path
from authapp.views import (
    login_view, logout_view, admin_dashboard,
    user_profile, home, delete_user, user_detail,
    add_user
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('user_profile/', user_profile, name='user_profile'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('user_detail/<int:user_id>/', user_detail, name='user_detail'),
    path('add_user/', add_user, name='add_user'),  # ✅ Nueva ruta
]
