'''
En este desafío, deberás implementar una función personalizada que emule 
el comportamiento del método map utilizando funciones de orden superior.

La función recibirá dos parámetros: una lista y una función (func). 
La lista contendrá un conjunto de elementos (números, objetos, cadenas, etc.), 
y la función se utilizará para realizar una acción específica en cada elemento 
de la lista. El objetivo es retornar una nueva lista con los resultados obtenidos 
de aplicar la función a cada elemento, de manera similar a como lo haría el 
método map.
'''

def my_map(list, func):
    return [func(i) for i in list]

print(my_map([1,2,3,4], lambda num: num * 2))
print(my_map([
    {"name": "michi", "age": 2},
    {"name": "firulais", "age": 6}
], lambda pet: pet["name"]))