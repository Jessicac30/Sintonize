from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('formulario/', views.formulario, name='formulario'), 
    path('quem_somos/', views.quem_somos, name='quem_somos'),  
]

