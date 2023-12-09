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