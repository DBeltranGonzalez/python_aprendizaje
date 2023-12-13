'''
En este desafío, debes implementar la lógica de la función find_set_intersection 
que encuentre la intersección de conjuntos en una lista de conjuntos.

Recibirás un único parámetro: una lista de conjuntos. La función debe encontrar 
la intersección de todos los conjuntos de la lista y devolver el resultado como 
un nuevo conjunto. Si la lista está vacía o no hay intersección entre los 
conjuntos, la función debe devolver un conjunto vacío.
'''

set_one = [
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
]

set_two = [
    {1, 2, 3, 4},
    {2, 4, 6, 8},
    {3, 6, 9, 12}
]

set_three = [
    {1,2,3,4},
    {2,3,4},
    {1,2,4},
    {2,3},
    {2}
]

set_four = [
    {1,2,3}
]

def find_set_intersection(sets):
    
    if len(sets) > 1:
        new_set = set(sets[0])

        for i in sets:
            new_set = i & new_set
        return(new_set)
    else:
        new_set = set()
        return(new_set)
    
print(find_set_intersection(set_one))
print(find_set_intersection(set_two))
print(find_set_intersection(set_three))
print(find_set_intersection(set_four))