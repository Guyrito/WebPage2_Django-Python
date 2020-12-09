"""webSite_Prueba2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views
from django.conf import settings 
from games import views as gameViews
from contact import views as contactViews

urlpatterns = [
    path('',views.home, name='home'),
    path('ps4/',gameViews.ps4, name='ps4'),
    path('steam/',gameViews.steam, name='steam'),
    path('page/',include('pages.urls')),
    path('contact/',contactViews.contact, name='contact'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('admin/',admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)