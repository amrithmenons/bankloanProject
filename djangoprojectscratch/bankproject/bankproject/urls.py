"""
URL configuration for bankproject project.

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

# from django.contrib import admin
# from django.urls import path, re_path,include
# #from django.conf.urls import url
# from bankapp.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('basic-information/', BasicInformationView.as_view(), name='basic_information'),
#     path('basic-info-account/', BasicInfoAccountView.as_view(), name='basic_info_account'),
#     path('users/', UserView.as_view(), name='user'),
#     path('admins/', AdminView.as_view(), name='admin'),
# ]
#     #path('',Reactview.as_view(), name="anything")

from django.contrib import admin
from django.urls import path, re_path,include
from django.urls import path
from bankapp.views import BasicInformationView, BasicInfoAccountView, UserView, AdminView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic-information/', BasicInformationView.as_view(), name='basic_information_list_create'),
    path('basic-information/<int:pk>/', BasicInformationView.as_view(), name='basic_information_detail'),
    path('basic-info-account/', BasicInfoAccountView.as_view(), name='basic_info_account_list_create'),
    path('basic-info-account/<int:pk>/', BasicInfoAccountView.as_view(), name='basic_info_account_detail'),
    path('users/', UserView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserView.as_view(), name='user_detail'),
    path('admins/', AdminView.as_view(), name='admin_list_create'),
    path('admins/<int:pk>/', AdminView.as_view(), name='admin_detail'),
]
