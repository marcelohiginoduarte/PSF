from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Farmacia import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Farmacia/', include('Farmacia.urls')),
]

