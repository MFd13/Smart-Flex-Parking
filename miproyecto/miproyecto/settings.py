from pathlib import Path

# 📌 Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 📌 Seguridad
SECRET_KEY = 'django-insecure-*1@xshxo38hy0b2^p-9-^-rm&o2+g$!wy6mh!04r27nce7b@vj'
DEBUG = True
ALLOWED_HOSTS = []

# 📌 Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authapp',
]

# 📌 Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miproyecto.urls'

# 📌 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miproyecto.wsgi.application'

# 📌 Base de datos - MongoDB Atlas con djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'estacionamiento',  # ✅ El nombre de tu base en Atlas
        'CLIENT': {
            'host': 'mongodb+srv://hiramquintanasoto:RViVqEazbdkUbeAB@cluster0.kilg0.mongodb.net/estacionamiento?retryWrites=true&w=majority',
            'username': 'hiramquintanasoto',
            'password': 'RViVqEazbdkUbeAB',
            'authSource': 'admin',
        }
    }
}



# 🔐 Reemplaza <USUARIO> y <PASSWORD> con los de tu base de datos Atlas
# Ejemplo:
# mongodb+srv://admin123:miclave@cluster0.kilg0.mongodb.net/estacionamiento...

# 📌 Usuario personalizado
AUTH_USER_MODEL = 'authapp.CustomUser'

# 📌 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 📌 Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📌 Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# 📌 Archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# 📌 Campo de clave primaria
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📌 Login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_profile'
LOGOUT_REDIRECT_URL = 'login'
