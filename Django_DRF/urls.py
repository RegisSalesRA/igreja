"""Django_DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from apps.igreja.urls import igrejaUrl
from apps.membros.urls import membrosUrl
from apps.registros.urls import registroUrl
from rest_framework.authtoken import views

urlpatterns = [
    # API
    path('sede/', include(igrejaUrl.urls)),
    path('membro/', include(membrosUrl.urls)),
    path('registros/', include(registroUrl.urls)),
    # API END

    path('admin/', admin.site.urls),
    path('', include('apps.igreja.urls')),
    path('index2/', include('apps.membros.urls')),
    path('index3/', include('apps.registros.urls')),

    #  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #   path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
