'''
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.
Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. 
Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, 
manteniendo el orden en el que aparecen en la lista de entrada.
'''

def find_famous_cat(cats):
    popular = []
    max = 0
    for cat in cats: # Para recorrer la tupla cats
        suma_followers = 0
        for i in cat['followers']: # Para hacer el conteo de seguidores
            suma_followers += i
        cat['total'] = suma_followers # Nuevo valor en el diccionario con el total de seguidores
        if suma_followers >= max:
            max = suma_followers
    
    for cat in cats:
        if cat['total'] == max:
            popular.append(cat['name']) # Agregar a la lista al o los gatos más populares
    return(popular)

cats = (
    [
        {
            "name": "Luna",
            "followers": [500, 200, 300]
        },
        {
            "name": "Michi",
            "followers": [100, 300]
        }
    ]
)

kitties = ([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

print(find_famous_cat(cats))
print(find_famous_cat(kitties))
