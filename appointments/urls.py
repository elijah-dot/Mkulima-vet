from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view(), name='appointment'),   
    path('appointments/', views.appointListView.as_view(), name='appointments')   
]
