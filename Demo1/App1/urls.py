from rest_framework import routers
from .views import AuthViewSet, ProfileView

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')
router.register('api/profile', ProfileView, basename='profile')


urlpatterns =router.urls
