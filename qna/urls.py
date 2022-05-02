from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import QnaViewSet



router= DefaultRouter()
router.register('qna', QnaViewSet)


urlpatterns= [
	path('',include(router.urls)),
]