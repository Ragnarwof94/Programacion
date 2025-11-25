# EJERCICIOS POR TIPO DE DATO — Contexto Empresarial
"""
1. Ejercicios para el tipo de dato int (entero)
Empresa: "LogiExpress" — Empresa de envíos nacionales
Situación:
El departamento de operaciones necesita calcular la cantidad total de paquetes procesados en una jornada.
Ejercicio:
Pide al usuario ingresar:
Cantidad de paquetes enviados en la mañana
Cantidad de paquetes enviados en la tarde
Cantidad de paquetes enviados en la noche
Objetivo:
Suma los valores y muestra el total de paquetes procesados.
"""

# ➡️ Solicitar al usuario la cantidad de paquetes enviados en cada turno
paquetes_manana = input("Ingrese la cantidad de paquetes enviados en la mañana: ")
# ➡️ Convertir la entrada de texto a un número entero
paquetes_manana = int(paquetes_manana)
# ➡️ Repetir para la tarde y la noche
paquetes_tarde= input("Ingrese la cantidad de paquetes enviados en la tarde: ")
# ➡️ Convertir la entrada de texto a un número entero
paquetes_tarde = int(paquetes_tarde)
# ➡️ Repetir para la noche
paquetes_noche = input("Ingrese la cantidad de paquetes enviados en la noche: ")
# ➡️ Convertir la entrada de texto a un número entero
paquetes_noche = int(paquetes_noche)

# ➡️ Calcular el total de paquetes procesados en la jornada
total = paquetes_manana + paquetes_tarde + paquetes_noche
# ➡️ Mostrar el total en consola
# ➡️ Usamos print() para mostrar el mensaje en consola.
# ➡️ Se concatenan textos y variables usando comas para separar los elementos.
# ➡️   No se usan signos de suma (+) para concatenar en print(), ya que las comas manejan la separación automáticamente.
print("Total de paquetes procesados en la jornada:", total)