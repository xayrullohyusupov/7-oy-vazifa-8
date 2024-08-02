from django.urls import path
from . import views

urlpatterns = [
    path('banner_list/', views.banner_list, name='banner_list'),
    path('banner/<int:id>/', views.banner_detail, name='banner_detail'),
    path('banner/create/', views.banner_create, name='banner_create'),
    path('banner/update/<int:id>/', views.banner_update, name='banner_update'),
    path('banner/delete/<int:id>/', views.banner_delete, name='banner_delete'),
]
