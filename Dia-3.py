# Condicionales
'''
En este desafío de Python, debes crear la lógica de la función is_leap_year, 
que determina si un año es bisiesto o no. Un año es bisiesto si cumple con las
siguientes condiciones:

- Es divisible por 4, pero no por 100.
- Si es divisible por 100 debe serlo por 400 también.
'''
def is_leap_year(year):
    if(year <= 0):
        return False
    elif year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
    
mi_anio = is_leap_year(2000)
print(mi_anio)
mi_anio = is_leap_year(-2024)
print(mi_anio)
mi_anio = is_leap_year(1984.25)
print(mi_anio)

# Ciclos
'''
En este desafío, debes dibujar un triángulo equilatero usando bucles.
'''

# Sin retornar variable (impresión directa desde la función)
def printTriangle(size, character):
    # Tu código aquí 👈
    contador = 1
    char_print = 1
    while contador <= size:
        print((' ') * (size - contador) + (character * char_print)) 
        contador += 1
        char_print += 2

printTriangle(3, '_')
printTriangle(6, '$')

# Retornando variable de cadena
def print_triangle(size, character):

    triangle: str = ''
    contador = 1
    while contador <= size:
        triangle += ((' ') * (size - contador)) 
        triangle += (character * (contador ** 2 - (contador - 1) ** 2))
        if contador < size:
            triangle += '\n'
        contador += 1
    return triangle

print(print_triangle(4, 'C'))
print(print_triangle(7, '&'))