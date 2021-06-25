from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from core.views import MusicViewSet


router = routers.DefaultRouter()
router.register(r'music', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
