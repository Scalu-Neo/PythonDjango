import requests
from django.http import JsonResponse

def get_cep_info(request, cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    return JsonResponse(data)