from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginApiView, ProfileViewSet


router= DefaultRouter()
router.register('user',UserViewSet)
router.register('profile',ProfileViewSet)



urlpatterns= [
	path('',include(router.urls)),
	path('login/', UserLoginApiView.as_view()),
]