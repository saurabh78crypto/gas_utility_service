from django.urls import path
from . import views

app_name = 'admin_panel'

# Restrict access to admin panel
def is_admin(user):
    return user.is_superuser

urlpatterns = [
    path('', views.all_requests, name='all_requests'),
    path('update/<int:request_id>/', views.update_request, name='update_request'),
]
