from django.shortcuts import render
import requests
from requests.exceptions import Timeout

def home(request):
    try:
        # O timeout está configurado para 1 segundo
        response = requests.get("http://equilibra-production.up.railway.app", timeout=1)
        # Apenas tenta acessar o JSON se a requisição for bem-sucedida
        frase_efeito = response.json().get("frase", "Frase padrão caso falhe a API.")
    except Timeout:
        # Caso a API demore mais de 3 segundos, usamos a frase padrão
        frase_efeito = "Frase padrão caso a API tenha demorado mais de 1 segundos."
    except requests.RequestException as e:
        # Para outros erros de requisição, use a frase padrão
        frase_efeito = "Frase padrão caso a API falhe."

    context = {
        'frase_efeito': frase_efeito,
        'logo_url': 'caminho/para/sua/logo.png', 
    }
    return render(request, 'pages/home.html', context)

def formulario(request):
    return render(request, 'pages/formulario.html')

def questionario(request):
    return render(request, 'pages/questionario.html')

def trilha_conhecimento(request):
    return render(request, 'pages/trilha_conhecimento.html')

def quem_somos(request):
    return render(request, 'pages/quem_somos.html')

def contatos(request):
    return render(request, 'pages/contatos.html')

def pesquisar(request):
    return render(request, 'pages/pesquisar.html')

def pomodoro_view(request):
    return render(request, 'pomodoro.html')  

def tecnicas_tcc_view(request):
    return render(request, 'tecnicas_tcc.html') 