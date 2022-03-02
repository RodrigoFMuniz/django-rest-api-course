"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import Pontos_Turisticos_ViewSet
from atracoes.api.viewsets import Atracoes_Viewset
from localizacao.api.viewsets import Localizacao_Viewset

router = routers.DefaultRouter()
router.register(r'pontos_turisticos', Pontos_Turisticos_ViewSet)
router.register(r'atracoes', Atracoes_Viewset)
router.register(r'localizacao',Localizacao_Viewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]


