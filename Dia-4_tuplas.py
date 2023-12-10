'''
En este desafío, te encuentras trabajando para una empresa de transporte 
de carga que necesita llevar un registro de los paquetes que se envían en 
cada viaje. Para ello, se te proporcionará una lista de tuplas, cada una 
de las cuales representará un paquete y tendrá las siguientes propiedades:
    (id, weight, destination)
A partir de esta información, debes crear una función que calcule el peso 
total de los paquetes, así como la cantidad de paquetes que se enviarán a 
cada destino. Para ello, debes retornar un nuevo diccionario que tenga las 
siguientes propiedades:
    - "total_weight": El peso total de los paquetes.
    - "destinations": Un diccionario con los destinos como claves y la cantidad de 
    paquetes como valores.
'''

packages = [
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]

def get_packages_info(packages):
    
    result = {
        'total_weight': '',
        'destinations': {}
    }

    paises = []
    new_list = []
    total_weight = 0
    
    for pack in packages:
        total_weight += pack[1]
        paises.append(pack[2])
        if pack[2] not in new_list:
            new_list.append(pack[2])

    pais = tuple(paises)
    for i in new_list:
        result['destinations'][i] = pais.count(i)

    result['total_weight'] = round(total_weight,2)
    return(result)

print(get_packages_info(packages))