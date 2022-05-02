"""reds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
	home,
	guest_login,
	)

# https://docs.djangoproject.com/en/4.0/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('blog/', include('blog.urls')),
    path('api-price/', include('price.urls')),
    path('api-users/', include('users.urls')),
    path('api-qna/', include('qna.urls')),
    path('api-info/', include('info.urls')),
    path('api-search/', include('search.urls')),

    #django-allauth,
    path('accounts/', include('allauth.urls')),
    #かんたんログイン用
    path('guest_login/', guest_login, name='guest_login'),
]



# Serving files uploaded by a user during development
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 