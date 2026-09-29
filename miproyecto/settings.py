from pathlib import Path

# pymysql: el conector que instalaste con pip
import pymysql
# Hace que Django use pymysql como si fuera el driver oficial de MySQL para Python
pymysql.install_as_MySQLdb()

# config: función de python-decouple que lee valores del archivo .env
# Csv: convierte un valor separado por comas del .env en una lista de Python
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: ya no queda escrita en el código — se lee del .env / de Render
SECRET_KEY = config('SECRET_KEY')

# DEBUG: default=False es la opción segura si la variable no está definida
# cast=bool convierte el texto "True"/"False" del .env en un booleano real de Python
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS: lista de dominios que Django acepta atender; Csv() la separa por comas
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    # SecurityMiddleware: agrega cabeceras de seguridad básicas a cada respuesta
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoiseMiddleware: nueva línea — debe ir justo después de SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # SessionMiddleware: habilita las sesiones (login, carrito, etc.)
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CommonMiddleware: ajustes generales de peticiones/respuestas
    'django.middleware.common.CommonMiddleware',
    # CsrfViewMiddleware: protege los formularios contra ataques CSRF
    'django.middleware.csrf.CsrfViewMiddleware',
    # AuthenticationMiddleware: asocia cada petición con el usuario logueado (si hay uno)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # MessageMiddleware: habilita mensajes flash de una sola vista (ej. "guardado con éxito")
    'django.contrib.messages.middleware.MessageMiddleware',
    # XFrameOptionsMiddleware: evita que tu sitio se cargue dentro de un <iframe> ajeno
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miproyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Base de datos MySQL remota en Aiven, leída desde el archivo .env
DATABASES = {
    'default': {
        # ENGINE: qué motor de base de datos usar — mysql en vez del sqlite3 por defecto
        'ENGINE': 'django.db.backends.mysql',
        # NAME: nombre de la base de datos, leído de la variable DB_NAME del .env
        'NAME': config('DB_NAME'),
        # USER: usuario de conexión, leído de DB_USER
        'USER': config('DB_USER'),
        # PASSWORD: contraseña de conexión, leída de DB_PASSWORD
        'PASSWORD': config('DB_PASSWORD'),
        # HOST: servidor donde vive la base de datos, leído de DB_HOST
        'HOST': config('DB_HOST'),
        # PORT: puerto de conexión; default='3306' se usa solo si DB_PORT no está en el .env
        'PORT': config('DB_PORT', default='3306'),
        # OPTIONS: Aiven exige que la conexión venga cifrada (SSL)
        'OPTIONS': {'ssl': {'ssl-mode': 'REQUIRED'}},
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Hermosillo'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

# STATIC_ROOT: carpeta donde collectstatic junta todos los archivos estáticos antes de publicar
STATIC_ROOT = BASE_DIR / 'staticfiles'

# STORAGES: le dice a Django que use whitenoise para comprimir y versionar esos archivos
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
