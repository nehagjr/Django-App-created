"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index
from app import views as v1
from app1 import views as v2
from app2 import views as v3
from app3 import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index,name='index'),
    path('home1/',v1.index,name='index1'),
    path('home2/',v2.index,name='index2'),
    path('home3/',v3.index,name='index3'),
    path('home4/',v4.index,name='index4'),
]
