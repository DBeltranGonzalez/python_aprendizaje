'''
En este desafío, debes crear una función llamada count_words_by_length 
que recibe una lista de palabras y devuelve un diccionario que mapea la 
longitud de las palabras a la cantidad de palabras que tienen esa longitud.
'''

def count_words_by_length(words):

  conteo_letras = {len(fruit): sum(1 for i in words if len(i) == len(fruit))
                   for(fruit) in words}
  return(conteo_letras)

count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])