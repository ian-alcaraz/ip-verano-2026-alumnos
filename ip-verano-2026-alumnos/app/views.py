# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

def home(request):
    """
    Vista principal que muestra la galería de personajes de Los Simpsons.
    
    Esta función debe obtener el listado de imágenes desde la capa de servicios
    y también el listado de favoritos del usuario, para luego enviarlo al template 'home.html'.
    Recordar que los listados deben pasarse en el contexto con las claves 'images' y 'favourite_list'.
    """
    images = services.getAllImages()
    favourite_list = [  ]

    
    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    """
    Busca personajes por nombre.
    
    Se debe implementar la búsqueda de personajes según el nombre ingresado.
    Se debe obtener el parámetro 'query' desde el POST, filtrar las imágenes según el nombre
    y renderizar 'home.html' con los resultados. Si no se ingresa nada, redirigir a 'home'.
    """
    query = request.POST.get('query', '') # busca el query 

    if query !='': # si el query es distinto que vacio, entra en el if 
        images = services.filterByCharacter(query) # filtra el por el nombre 

        favourite_list = []
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list }) # devuelve el request
    else:
        return redirect('home') # si no escribio nada, lo devuelve al home 


    pass

def filter_by_status(request):
    """
    Filtra personajes por su estado (Alive/Deceased).
    
    Se debe implementar el filtrado de personajes según su estado.
    Se debe obtener el parámetro 'status' desde el POST, filtrar las imágenes según ese estado
    y renderizar 'home.html' con los resultados. Si no hay estado, redirigir a 'home'.
    """

    status = request.POST.get('status', '') # busca el estado
    if status != '': # si el estado es distinto a vacio entra en el condicional
        images = services.filterByStatus(status)# filtra por el estado
        favourite_list=[]
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list }) # retorna el resultado
    else:
        return redirect('home') # si esta vacio te devuelve a home 
    pass

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    """
    pass

@login_required
def saveFavourite(request):
    """
    Guarda un personaje como favorito.
    """
    pass

@login_required
def deleteFavourite(request):
    """
    Elimina un favorito del usuario.
    """
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')