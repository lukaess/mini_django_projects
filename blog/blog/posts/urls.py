from django.urls import path
from . import views
import posts


urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<str:pk>', views.post, name = 'post')
]