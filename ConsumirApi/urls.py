from django.urls import path
from . import views

urlpatterns = [
    path('cep/<str:cep>/', views.get_cep_info, name='get_cep_info'),
   
]
