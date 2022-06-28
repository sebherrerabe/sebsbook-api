from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('api/')),
    path('api/', include('api.urls')),
]
