"""
Un Diccionario en Python es una estructura de datos que permite almacenar pares de clave-valor. Cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que sus elementos pueden ser modificados, añadidos o eliminados después de su creación. Se definen utilizando llaves {} y los pares clave-valor se separan por dos puntos (:).
"""

# Ejemplos de diccionarios
#➡️ Diccionario que mapea números a sus representaciones en palabras
#➡️ Clave: número entero, Valor: cadena de texto
#➡️ Diccionario de traducción de inglés a español
#➡️ Clave: palabra en inglés, Valor: palabra en español
#➡️ Diccionario que representa información de una persona
#➡️ Clave: atributo de la persona, Valor: valor del atributo
persona = {
    #➡️ Clave: "nombre", Valor: "Ana Maria"
    "nombre": "Ana Maria",
    #➡️ Clave: "edad", Valor: 28
    "edad": 28,
    #➡️ Clave: "ciudad", Valor: "Medellín"
    "ciudad": "Medellín"
}

#➡️ Imprime el diccionario que representa la información de una persona
#➡️ Muestra las claves y valores almacenados en el diccionario
#➡️ La función print() muestra el contenido del diccionario en la consola
#➡️ Al ejecutar esta línea, se verá la representación completa del diccionario persona
#➡️ La salida será: {'nombre': 'Ana Maria', 'edad': 28, 'ciudad': 'Medellín'}
print(persona)