from django.urls import path
from . import views

urlpatterns = [
    path('info_list/', views.info_list, name='info_list'),
    path('infos/<int:id>/', views.info_detail, name='info_detail'),
    path('infos/create/', views.info_create, name='info_create'),
    path('infos/<int:id>/update/', views.info_update, name='info_update'),
    path('infos/<int:id>/delete/', views.info_delete, name='info_delete'),
]
