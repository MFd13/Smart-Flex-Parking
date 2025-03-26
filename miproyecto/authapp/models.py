from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, matricula, password=None, **extra_fields):
        if not matricula:
            raise ValueError("El usuario debe tener una matrícula")
        user = self.model(matricula=matricula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('type', 'Admin')  # Autoasigna tipo Admin
        return self.create_user(matricula, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    matricula = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    type = models.CharField(max_length=10, default='Normal')  # Admin o Normal

    objects = CustomUserManager()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.matricula
