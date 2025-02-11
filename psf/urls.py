from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Farmacia.views import EstoqueFarmaciaViewSet


router = DefaultRouter()
router.register(r'farmacia', EstoqueFarmaciaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
