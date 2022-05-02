from email.mime import base
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TagViewSet, InfoViewSet


router= DefaultRouter()
router.register('tag', TagViewSet, basename='tag')
router.register('info', InfoViewSet, basename='info')


urlpatterns= [
	path('',include(router.urls)),
]