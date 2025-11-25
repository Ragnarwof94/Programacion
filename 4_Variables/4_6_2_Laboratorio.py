"""
2. Ejercicios para el tipo de dato float (decimal)
Empresa: "AquaPure" — Purificadora de agua
Situación:
El laboratorio debe registrar la cantidad de litros purificados en distintos tanques.
Ejercicio:
Pide al usuario:
Litros purificados en el tanque A
Litros purificados en el tanque B
Objetivo:
Calcular la producción total con decimales.
"""
# ➡️ Solicitar al usuario los litros purificados en cada tanque
tanque_a = input("Ingrese los litros purificados en el tanque A: ")
# ➡️ Convertir la entrada de texto a un número decimal (float)
tanque_a = float(tanque_a)
# tanque_a = float(input("Ingrese los litros purificados en el tanque A: "))
# ➡️ Repetir para el tanque B
tanque_b = input("Ingrese los litros purificados en el tanque B: ")
# ➡️ Convertir la entrada de texto a un número decimal (float)
tanque_b = float(tanque_b)
# ➡️ Calcular la producción total de litros purificados
total_produccion = tanque_a + tanque_b
# ➡️ Mostrar la producción total en consola
# ➡️ Usamos print() para mostrar el mensaje en consola.
# ➡️ Se concatenan textos y variables usando comas para separar los elementos.
# ➡️   No se usan signos de suma (+) para concatenar en print(), ya que las comas manejan la separación automáticamente.
print("Producción total de litros purificados:", total_produccion)