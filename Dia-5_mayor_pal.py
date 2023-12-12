'''
En este desafío, debes crear una función que encuentre el palíndromo más largo en una 
lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la 
lista, la función debe devolver None. Si hay más de un palíndromo con la misma longitud 
máxima, debes devolver el primer palíndromo encontrado en la lista.
'''

lista_palindromo = ['racecar', 'reconocer', 'anita lava la tina']
lista2 = ['calma', 'acera', 'fuerte']

def find_largest_palindrome(words):
    reverse = ''
    mayor = 0
    largest = ''
    for i in words:
        size = 0
        reverse = i[::-1]
        if i == reverse:
            size = len(i)
            if size > mayor:
                mayor = size
                largest = i
    if mayor == 0:
        return None
    else:
        return largest

print(find_largest_palindrome(lista_palindromo))
print(find_largest_palindrome(lista2))