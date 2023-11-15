'''
En este desafío tendrás que calcular la propina que deben dejar 
los clientes de un restaurante en función de su consumo.
'''

# Función para calcular la propina

def calculate_tip(bill_amount, tipPercentage):
   # Tu código aquí 👈
   tipPercentage /= 100
   tip = round((bill_amount * tipPercentage), 2)
   return tip

print(calculate_tip(100,10))
print(calculate_tip(1524.33,25))