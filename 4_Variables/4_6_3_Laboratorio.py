"""
3. Ejercicios para el tipo de dato str (texto)
Empresa: "CustomerFirst" — Call Center de atención al cliente
Situación:
El supervisor necesita registrar el nombre del agente y el nombre del cliente atendido.
Ejercicio:
Pide al usuario:
Nombre del agente
Nombre del cliente
Objetivo:
Mostrar un mensaje combinando textos.
"""
# ➡️ Solicitar al usuario el nombre del agente y del cliente
nombre_agente = input("Ingrese el nombre del agente: ")
# ➡️ Solicitar el nombre del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")
# ➡️ Mostrar el mensaje combinando los textos ingresados
# ➡️ Usamos print() para mostrar el mensaje en consola.
# ➡️ Se concatenan textos y variables usando comas para separar los elementos.
# ➡️   No se usan signos de suma (+) para concatenar en print(), ya que las comas manejan la separación automáticamente.
print("El agente: ", nombre_agente, " ha atendido al cliente: ", nombre_cliente + ".")