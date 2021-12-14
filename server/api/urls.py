from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('generate/<int:userId>/', views.generate, name='generate'),
    path('usetoken/<int:userId>/<token>/', views.usetoken, name='usetoken'),
    path('test/', views.test, name='test' )
]