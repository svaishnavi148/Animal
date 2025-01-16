"""Recommendationsystem URL Configuration

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
from django.urls import path
from . import index
##from . import UserDashboard
##from . import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myregister', index.register),
    path('index', index.inde),
    path('aboutus',index.about),
    path('service',index.service),
    path('registration',index.doregister),
    path('hospitalregister',index.hospitalregister),
    path('signup',index.dologin),
    path('showhospital',index.showhospital),
    path('findhospital',index.findhospital),
    path('',index.login),
    path('logout',index.logout),
    path('adminhospital',index.dataset),
    path('viewuserprofile',index.viewuser),
    path('viewpredicadmin',index.viewpredicadmin),
    path('dashremove',index.dashremove),
    #path('index',index.index),
    path('livepred',index.livepred),
    path('prevpred',index.prevpred),
    path('dashboard',index.dashboard),
    path('remove',index.removeproduct),
    path('doremove',index.doremoveproduct),
    path('myprofile',index.myprofile),
    path('btn',index.algocall),
    path('nanalyze',index.nanalyze),
          
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

