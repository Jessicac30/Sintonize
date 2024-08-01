from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('questionario/', views.questionario, name='questionario'), 
    path('formulario/', views.formulario, name='formulario'), 
    path('trilha_conhecimento/', views.trilha_conhecimento, name='trilha_conhecimento'),  
    path('quem_somos/', views.quem_somos, name='quem_somos'),  
    path('contatos/', views.contatos, name='contatos'),  
    path('pesquisar/', views.pesquisar, name='pesquisar'),  
    path('quem_somos/', views.quem_somos, name='quem_somos'),
    path('contatos/', views.contatos, name='contatos'),
    path('pomodoro/', views.pomodoro_view, name='pomodoro'),  
    path('tecnicas_tcc/', views.tecnicas_tcc_view, name='tecnicas_tcc'),  
    
]

