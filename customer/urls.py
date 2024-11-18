from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
]

