"""marcajepersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from marcaje.views import añadir_usuario, control_panel, marcaje_entrada, marcaje_salida

urlpatterns = [
    path('', control_panel),
    path('admin/', admin.site.urls),
    path('add_nuevo_usuario/', añadir_usuario),
    path('marcaje_entrada/',marcaje_entrada),
    path('marcaje_salida/',marcaje_salida),
    path('control_panel/',control_panel)
]
