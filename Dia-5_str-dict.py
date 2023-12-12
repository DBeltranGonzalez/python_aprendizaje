'''
En este desafío deberás implementar la lógica de una función que cuente la cantidad 
de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, 
es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.
'''

texto = 'Hola mundo'

def count_letters(phrase):
    
    result = {}
    for i in phrase:
        result[i] = phrase.count(i)
    print (result)

count_letters(texto)