'''
En este desafío implementarás una función que filtre los mensajes de un usuario 
específico. La función filter_user_messages recibirá dos parámetros:
    messages: una lista de mensajes
    user: un nombre de usuario.
Debe devolver una nueva lista que contenga solo los mensajes del usuario especificado.

La lista messages contiene diccionarios con información sobre cada mensaje, incluyendo 
el remitente ('sender') y el contenido del mensaje ('content').

En caso de no encontrar mensajes del usuario deberá retornar una lista vacía []
'''

def filter_user_messages(messages, user):
    rest = [m for m in messages if user == m['sender']] 
    #resultado = list(filter(lambda i: i['sender'] == user, messages['content']))
    return(rest)

messages = [
    {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
    {'sender': 'Bob', 'content': '¡Bien, gracias!'},
    {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
    {'sender': 'Charlie', 'content': 'Hola a todos.'},
    {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

# Resultado con lambda function
filt_user_messages = lambda messages, user: [m for m in messages if user == m['sender']]

print(filt_user_messages(messages, 'Charlie'))
print(filter_user_messages(messages, 'Andy'))
print(filter_user_messages(messages, 'Alice'))
