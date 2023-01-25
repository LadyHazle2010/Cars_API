# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-376@eo^rupywr24_dv7#xdya24eghca@!lyw&2%xm)07=sj3ga'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Taujofmylife06',
    }
}