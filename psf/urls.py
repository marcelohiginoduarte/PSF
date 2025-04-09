from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Farmacia import urls
from Farmacia.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('Farmacia/', include('Farmacia.urls')),
]

