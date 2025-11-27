numero1 = input("Ingrese el primer número: ")
# ➡️ input() muestra el mensaje en consola y espera que el usuario escriba un valor.
# ➡️ Lo que escribe el usuario se almacena en la variable numero1.
# 📌 Todo lo que devuelve input() es texto (string), no un número.

numero1 = int(numero1)
# ➡️ int() convierte el valor de texto a un número entero.
# ➡️ Esto es necesario para poder hacer operaciones matemáticas.
# ⚠️ Si el usuario no escribe un número válido (ej: "hola"), el programa dará error.

numero2 = input("Ingrese el segundo número: ")
# ➡️ Se pide el segundo dato al usuario.
# ➡️ También se almacena primero como texto en la variable numero2.

numero2 = int(numero2)
# ➡️ Se convierte el texto ingresado a un número entero.
# ➡️ Ahora se pueden sumar los valores.

print("La suma es: ", numero1 + numero2)
# ➡️ print() muestra un mensaje y el resultado de la operación.
# ➡️ numero1 + numero2 realiza la suma aritmética de los dos valores convertidos.

# 🧠 Ejemplo al ejecutarse
# Usuario ingresa:
# Ingrese el primer número: 10
# Ingrese el segundo número: 5
# Salida:
# La suma es:  15