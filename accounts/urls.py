from django.urls import path
from accounts import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    path('staff_register/', views.staff_register, name='staff_register'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staff_logout/', views.staff_logout, name='staff_logout'),
]