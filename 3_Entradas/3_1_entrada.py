nombre = input("¿Cual es tu nombre? ")
# ➡️ input() muestra el texto entre comillas en la consola y espera que el usuario escriba algo.
# ➡️ Lo que escriba el usuario se guarda en la variable nombre.
# 📌 nombre será una cadena (string).

fruta = input("¿Cual es tu fruta favorita? ")
# ➡️ Nuevamente se usa input() para pedir información.
# ➡️ El texto que escriba el usuario se guarda en la variable fruta.

print("Hola "+nombre+" tu fruta favorita es "+fruta)
# ➡️ La función print() muestra texto en la consola.
# ➡️ Se hace concatenación: unir textos con el operador +.
# ➡️ Se imprime el mensaje final combinando el texto fijo + las variables.

# 📌 Ejemplo si el usuario escribe:

# nombre → Carlos

# fruta → Mango

# 📦 Comentario multilínea (explicativo del ejercicio)

"""
El usuario *******, tiene un problema con ********** y la fecha es *******.

Lo que muestra el programa al ejecutarse es:

El usuario Carlos Andres, tiene un problema con su computadora y la fecha es 15 de junio de 2024.

3 Cajitas:
1. Nombre del usuario
2. Problema del usuario
3. Fecha

El usuario ___________, tiene un problema con ____________ y la fecha es ____________.
"""
# ➡️ Este bloque está entre triple comillas (""")
# 📌 Es una cadena multilínea sin usar → Python la ignora.
# 👉 Se usa como explicación o documentación para el programador.

# 🧠 Explica un posible ejercicio:

# Guardar nombre

# Guardar problema

# Guardar fecha
# Y luego imprimir una frase completa con esos datos.

# 📘 Segundo comentario multilínea (explicación técnica)
"""
1. ¿Como comprobar que se puede ejecutar el código?
1.1 ¿Está instalado python?
    - SI
    - NO -> Instalar python
2. ¿Dónde ejecutar el código?
    - En la terminal
    - En un editor de código
3. Mostrar el código y ejecutarlo
"""
# ➡️ Otro bloque de texto multilínea.
# 👉 Funciona como guía o instrucciones previas al uso del código.


# 🧠💡 Notas importantes
# ✔️ input() siempre devuelve un texto
# Incluso si escribes números, serán cadenas.
# Ejemplo: si escribes 50, Python lo ve como "50".

# ✔️ Concatenación con +
# Solo funciona si todo es texto (string).
# Si mezclas texto + número → ❗ error.

# ✔️ Triple comillas no son comentarios “reales”
# Python no tiene comentarios multilínea directos.

# Lo correcto sería usar # muchas veces.

# Las triple comillas → crean strings multilínea.

# 📌 Usadas como documentación o docstrings.

# SOLUCIÓN AL EJERCICIO PROPUESTO

# Se pide el nombre del usuario y se guarda en la variable "nombre"
nombre = input("¿Cuál es tu nombre? ")

# Se pide el problema del usuario y se guarda en la variable "problema"
problema = input("¿Cuál es tu problema? ")

# Se pide la fecha y se guarda en la variable "fecha"
fecha = input("¿Cuál es la fecha? ")

# Se imprime el resultado concatenando los valores ingresados
print("El usuario " + nombre + ", tiene un problema con " + problema + " y la fecha es " + fecha + ".")
# ➡️ Aquí se resuelve el ejercicio propuesto en el comentario multilínea.
# ➡️ Se usan las variables nombre, problema y fecha para crear la frase completa.