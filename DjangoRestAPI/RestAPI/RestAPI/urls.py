from django import urls
from django.contrib import admin
from django.urls import path, include
import rest_framework
from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name = 'test'),
    path('api/token/', obtain_auth_token, name = 'obtain'),
]
