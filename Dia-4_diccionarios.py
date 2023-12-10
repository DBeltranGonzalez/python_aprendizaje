'''
En este desafío deberás calcular el promedio general de una clase, así como el 
promedio individual de cada estudiante.
Para ello, se te proporcionará una lista de diccionarios, cada uno de 
los cuales representará a un estudiante y tendrá las siguientes propiedades:
    "name": El nombre del estudiante
    "grades": Las notas de cada materia del estudiante
A partir de esta información, debes retornar un nuevo diccionario que tenga 
la propiedad "class_average" con el promedio de la clase y una lista de "students" 
con los estudiantes y sus promedios individuales.
'''

notas_alumnos = ([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])

def get_student_average(students):
    # Tu código aquí 👈
    total_alumnos = 0
    avg_global = 0
    resultado = {}
    for estudiante in students:
        total_notas = len(estudiante['grades'])
        avg_ind = 0
        for i in estudiante['grades']:
            avg_ind += i
        estudiante['average'] = round(avg_ind / total_notas, 2)
        avg_global += estudiante['average']
        total_alumnos += 1
        del estudiante['grades']
    
    resultado['class_average'] = round(avg_global / total_alumnos, 2)
    resultado['students'] = students
    
    return(resultado)

print(get_student_average(notas_alumnos))