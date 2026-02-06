# capa de servicio/lógica de negocio

import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages():
    """
    Obtiene todas las imágenes de personajes desde la API y las convierte en objetos Card.
    
    Esta función debe obtener los datos desde transport, transformarlos en Cards usando 
    translator y retornar una lista de objetos Card.
    """
    json_collection = transport.getAllImages() # guardo la lista que devuelve transport
    cards = [] # creo una lista para almacenar las cards

    for personaje in json_collection: #recorro json collection
        objeto_card = translator.fromRequestIntoCard(personaje) #funcion para convertir info de la api a una card
        cards.append(objeto_card) # le agrego objeto card a la lista de cards
    return cards



    pass

def filterByCharacter(name):
    """
    Filtra las cards de personajes según el nombre proporcionado.
    
    Se debe filtrar los personajes cuyo nombre contenga el parámetro recibido. Retorna una lista de Cards filtradas.
    """ 
    all_cards = getAllImages() # llama a los datos de personajes en cards
    cards_filtrada = [] # lista vacia para almacenar los resultados de la busqueda
    for personaje in all_cards: # itearmos en las cards de personajes
        if name.lower() in personaje.name.lower(): # comparamos la iteracion con la busqueda, pasamos a minuscula todo para evitar problemas
            cards_filtrada.append(personaje) # si hay encuentra la correcta, se agrega el resultado a la nueva lista
    return cards_filtrada # retorna la lista 

    pass

def filterByStatus(status_name):
    """
    Filtra las cards de personajes según su estado (Alive/Deceased).
    
    Se deben filtrar los personajes que tengan el estado igual al parámetro 'status_name'. Retorna una lista de Cards filtradas.
    """

    all_cards = getAllImages() # llamamos a los datos del pj en cards
    cards_filtrada =[] # creo una lista para almacenar
    for personaje in all_cards: # recorro la lista
        if personaje.status.lower() == status_name.lower(): # comparo si es el mismo estado Alive/Deceased
            cards_filtrada.append(personaje) # si es asi, lo agrego a la lista
    return cards_filtrada         # retorno la lista con pj del mismo estado
    pass

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    """
    Guarda un favorito en la base de datos.
    
    Se deben convertir los datos del request en una Card usando el translator,
    asignarle el usuario actual, y guardarla en el repositorio.
    """
    pass

def getAllFavourites(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    
    Si el usuario está autenticado, se deben obtener sus favoritos desde el repositorio,
    transformarlos en Cards usando translator y retornar la lista. Si no está autenticado, se retorna una lista vacía.
    """
    pass

def deleteFavourite(request):
    """
    Elimina un favorito de la base de datos.
    
    Se debe obtener el ID del favorito desde el POST y eliminarlo desde el repositorio.
    """
    pass