'''En este desafío, debes crear la lógica de la función 
find_words_with_two_vowels que encuentre las palabras que 
contienen exactamente dos vocales en una lista de palabras. 
Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función 
debe devolver una nueva lista que contenga todas las palabras de 
la lista original que cumplan con la condición mencionada anteriormente. 
En caso de no haber palabras que cumplan con esta condición deberás 
retornar una lista vacía.'''

def find_words_with_two_vowels(words):

  result = [element for element in words 
            if (element.count('a') + element.count('e') + element.count('i') + 
                element.count('o') + element.count('u') + element.count('A') + 
                element.count('E') + element.count('I') + 
                element.count('O') + element.count('U')) == 2]
  return(result)

print(find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
]))