from django.shortcuts import render
from .models import *
import requests
from django.http import JsonResponse

def precio_dolar_ves(request):
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        # Hacer la solicitud a la API
        response = requests.get(api_url)
        data = response.json()
        
        # Extraer la tasa de cambio para VES (Bolívares)
        tasa_ves = data.get('rates', {}).get('VES', 'No disponible')
        
        context = {
            'precio_usd_ves': tasa_ves,
            'fecha_actualizacion': data.get('date', 'N/A'),
            'fuente': 'ExchangeRate-API',
        }
        
        return render(request, 'shop/precio_dolar.html', context)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def index(request):
    categories = Category.objects.all()
    # categories = [
    #     {'name': 'Desayunos', 'image': 'shop/img/categories/desayunos.jpeg'},
    #     {'name': 'Café Caliente', 'image': 'shop/img/categories/cafe_caliente.jpeg'},
    #     {'name': 'Café Helado', 'image': 'shop/img/categories/cafe_helado.jpeg'},
    #     {'name': 'Pastelería', 'image': 'shop/img/categories/pasteleria.jpeg'},
    #     {'name': 'Bebidas', 'image': 'shop/img/categories/bebidas.jpeg'},
    #     {'name': 'Almuerzos', 'image': 'shop/img/categories/almuerzos.jpeg'},
    #     {'name': 'Tés e Infusiones', 'image': 'shop/img/categories/tes_infusiones.jpeg'},
    #     {'name': 'Postres Saludables', 'image': 'shop/img/categories/saludables.jpeg'},
    #     {'name': 'Smoothies', 'image': 'shop/img/categories/smoothies.jpeg'},
    #     {'name': 'Postres', 'image': 'shop/img/categories/postres.jpeg'},
    #     {'name': 'Bocadillos', 'image': 'shop/img/categories/bocadillos.jpeg'},
    #     {'name': 'Meriendas', 'image': 'shop/img/categories/waffles.jpeg'},
    # ]
    return render(request, 'shop/index.html', {'categories': categories})

def menu(request):
    return render(request, 'shop/menu.html')

# Create your views here.
