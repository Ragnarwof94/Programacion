"""
El print sirve para imprimir en consola.
Imprime el texto que se encuentra entre los paréntesis.
Cuando se imprime un texto, este debe ir entre comillas.
"""
# ➡️ Este bloque es una cadena multilínea (triple comillas).
# 📌 En este caso funciona como un comentario explicativo, porque no se usa ni se asigna a una variable.
# Python lo ignora al ejecutar el programa.


print("Carlos Andres")
#➡️ print() es una función que muestra texto en la consola.
# 👉 Aquí imprime el texto entre comillas "Carlos Andres".

print('Hola Mundo')
# ➡️ Igual que arriba, pero usando comillas simples ' '.
# Python permite comillas simples o dobles para strings.
# 👉 Imprime: Hola Mundo

print("¿Cual es tu fruta favorita?")
# ➡️ Se imprime una pregunta.
# 👉 Los caracteres especiales y tildes funcionan correctamente dentro de un string.

print('Mi fruta favorita es la "Fresa"')
# ➡️ El texto usa comillas dobles dentro del string.
# 👉 Por eso el string se encierra con comillas simples ' ' para que Python no se confunda.

print("Mi fruta favorita es la 'Fresa'")
# ➡️ Caso contrario:
# El string usa comillas simples dentro " ' "
# 👉 Por eso el texto se encierra con comillas dobles " ".


# 💡 Regla práctica:

# Si tu texto lleva ", usa '...'

# Si tu texto lleva ', usa "..."