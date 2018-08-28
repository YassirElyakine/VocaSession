from django.urls import path
from . import views

urlpatterns = [
    path('', views.VocaSession,name='VocaSession'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]