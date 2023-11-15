'''
En este desafío encontrarás una función llamada solution 
que recibe un parámetro llamado valor. Debes encontrar el 
tipo de dato del parámetro valor y retornarlo desde la función 
solution.
'''

# Función para retornar el tipo de dato
def found_type(value):
    tipo_variable = type(value)
    return tipo_variable

print(found_type(1))
print(found_type('Dieguillo'))
print(found_type(True))