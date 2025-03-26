from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def login_view(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        password = request.POST.get('password')
        user = authenticate(request, matricula=matricula, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "¡Bienvenido!")
            return redirect_user(user)
        else:
            messages.error(request, "Credenciales incorrectas.")
    return render(request, 'authapp/login.html')


def redirect_user(user):
    if hasattr(user, 'type'):
        if user.type == 'Admin':
            return redirect('admin_dashboard')
        return redirect('user_profile')
    return redirect('login')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('login')


@login_required
def home(request):
    return redirect_user(request.user)


@login_required
def user_profile(request):
    return render(request, 'authapp/user_profile.html', {'user': request.user})


@login_required
def admin_dashboard(request):
    if request.user.type != 'Admin':
        return redirect('home')
    users = CustomUser.objects.all()
    return render(request, 'authapp/admin_dashboard.html', {'users': users})


@login_required
def delete_user(request, user_id):
    if request.user.type != 'Admin':
        return redirect('home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, "Usuario eliminado.")
    return redirect('admin_dashboard')


@login_required
def user_detail(request, user_id):
    if request.user.type != 'Admin':
        return redirect('home')
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        new_type = request.POST.get('type')
        if new_type in ['Admin', 'Normal']:
            user.type = new_type
            user.save()
            messages.success(request, "Tipo de usuario actualizado.")
            return redirect('user_detail', user_id=user.id)

    return render(request, 'authapp/user_detail.html', {'user': user})


@login_required
def add_user(request):
    if request.user.type != 'Admin':
        return redirect('home')

    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        password = request.POST.get('password')
        tipo = request.POST.get('type')

        if matricula and password and tipo in ['Admin', 'Normal']:
            CustomUser.objects.create_user(matricula=matricula, password=password, type=tipo)
            messages.success(request, "Usuario agregado exitosamente.")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Datos inválidos. Asegúrate de completar todos los campos.")

    return render(request, 'authapp/add_user.html')
