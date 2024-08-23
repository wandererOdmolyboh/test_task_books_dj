from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.library.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

app_name = 'library'
