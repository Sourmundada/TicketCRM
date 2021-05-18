from django.urls import path
from tickets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin_home, name='admin_home'),
    path('staff/dashboard/', views.staff_home, name='staff_home'),
    path('<int:ticket_pk>/', views.view_ticket, name='view_ticket'),
    path('add_tickets/', views.add_tickets, name='add_tickets'),
    path('<int:ticket_pk>/update_ticket/', views.update_ticket, name='update_ticket'),
    path('<int:ticket_pk>/delete_ticket/', views.delete_ticket, name='delete_ticket'),
    path('staff_member/<int:user_pk>/', views.staff_tickets, name='staff_tickets'),
    path('add_file/', views.add_attachments, name='add_attachments'),
]