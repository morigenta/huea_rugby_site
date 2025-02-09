#!/bin/sh

if [ ! -f "/app/manage.py" ]; then
    echo "Creating new Django project..."
    cd /app
    django-admin startproject config .

    python manage.py startapp home
    mkdir -p static media templates

    echo "Configuring Django settings..."

    # 基本設定
    sed -i '1i import os' config/settings.py
    sed -i "s/SECRET_KEY = .*/SECRET_KEY = os.environ.get('SECRET_KEY')/" config/settings.py
    sed -i "s/DEBUG = True/DEBUG = int(os.environ.get('DEBUG', 0)) == 1/" config/settings.py
    sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')/" config/settings.py

    # INSTALLED_APPS
    sed -i "/INSTALLED_APPS = \[/a\    'home'," config/settings.py
    sed -i "/INSTALLED_APPS = \[/a\    'django_cleanup'," config/settings.py
    sed -i "/INSTALLED_APPS = \[/a\    'corsheaders'," config/settings.py
    sed -i "/INSTALLED_APPS = \[/a\    'rest_framework'," config/settings.py

    # MIDDLEWARE（既存のリストの先頭に追加）
    sed -i "/MIDDLEWARE = \[/a\    'corsheaders.middleware.CorsMiddleware'," config/settings.py

    # CORS設定（ファイル末尾に追加）
    echo "
# CORS settings
CORS_ALLOW_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'False') == 'True'
CORS_ALLOWED_ORIGINS = [origin for origin in os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',') if origin]
CORS_ALLOW_CREDENTIALS = os.environ.get('CORS_ALLOW_CREDENTIALS', 'False') == 'True'
" >> config/settings.py

    # データベース設定
    sed -i "s/'ENGINE': 'django.db.backends.sqlite3'/'ENGINE': 'django.db.backends.mysql'/" config/settings.py
    sed -i "s/'NAME': .*,/'NAME': os.environ.get('MYSQL_DATABASE'),/" config/settings.py
    sed -i "/DATABASES = {/,/}/ s/}$/    'USER': os.environ.get('MYSQL_USER'),\n        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),\n        'HOST': 'db',\n        'PORT': '3306',\n}/" config/settings.py

    # 言語とタイムゾーン
    sed -i "s/LANGUAGE_CODE = 'en-us'/LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'ja')/" config/settings.py
    sed -i "s/TIME_ZONE = 'UTC'/TIME_ZONE = os.environ.get('TIME_ZONE', 'Asia\/Tokyo')/" config/settings.py

    # 静的ファイルとメディア
    echo "
# Static files
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/app/static/')

# Media files
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/app/media/')

# Debug toolbar
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
" >> config/settings.py
fi

echo "Running migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser..."
python manage.py createsuperuser --noinput

echo "Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000