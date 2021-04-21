from rest_framework import routers
from django.urls import include, path
from core import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'games', views.GameViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
