"""
Este programa pide:
1. El precio de un producto (como cadena) y lo convierte a entero. Ok
2. El impuesto (como cadena) y lo convierte a entero. Ok
3. El descuento (como cadena) y lo convierte a flotante. Ok
4. Luego imprime los tipos de datos antes y después de la conversión. Ok
5. Imprimimos el total a pagar después de aplicar el impuesto y el descuento.
"""
# ➡️ Solicitar al usuario el precio, impuesto y descuento
precio = input("Ingrese el precio del producto: ")
# ➡️ Mostrar el tipo de dato antes de la conversión
print(type(precio))
# ➡️ Convertir la entrada de texto a un número entero
precio = int(precio)
# ➡️ Mostrar el tipo de dato después de la conversión
print(type(precio))
# ➡️ Repetir para el impuesto
impuesto = input("Ingrese el impuesto (en porcentaje): ")
# ➡️ Mostrar el tipo de dato antes de la conversión
print(type(impuesto))
# ➡️ Convertir la entrada de texto a un número entero
impuesto = int(impuesto)
# ➡️ Mostrar el tipo de dato después de la conversión
print(type(impuesto))
# ➡️ Repetir para el descuento
descuento = input("Ingrese el descuento (en porcentaje): ")
# ➡️ Mostrar el tipo de dato antes de la conversión
print(type(descuento))
# ➡️ Convertir la entrada de texto a un número decimal (float)
descuento = float(descuento)
# ➡️ Mostrar el tipo de dato después de la conversión
print(type(descuento))
# ➡️ Calcular e imprimir el total a pagar después de aplicar el impuesto y el descuento
# ➡️ Usamos print() para mostrar el mensaje en consola.
# ➡️ Se concatenan textos y variables usando comas para separar los elementos.
# ➡️   No se usan signos de suma (+) para concatenar en print(), ya que las comas manejan la separación automáticamente.
print("Total a pagar: =",precio+(precio*impuesto/100)-(precio*descuento/100))