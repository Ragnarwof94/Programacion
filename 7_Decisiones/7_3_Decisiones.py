# ➡️ Ejemplo de uso de estructuras condicionales if, elif y else
# ➡️ Se evalúa el valor de la variable 'mascota' para determinar qué mensaje mostrar
# ➡️ Si la mascota es 'gato', se muestra un mensaje específico
# ➡️ Si la mascota es 'perro', se muestra otro mensaje
# ➡️ Si la mascota es 'pez', se muestra otro mensaje diferente
# ➡️ Si la mascota no es ninguna de las anteriores, se muestra un mensaje genérico
mascota = 'perro'
# ➡️ Usamos el operador de igualdad (==) para comparar valores
# ➡️ Si la condición del if es verdadera, se ejecuta el bloque de código indentado debajo del if
# ➡️ Si la condición del if es falsa, se evalúa la siguiente condición elif
# ➡️ Si ninguna condición es verdadera, se ejecuta el bloque debajo del else
if mascota == 'gato':
    # ➡️ Si la condición es verdadera, se ejecuta este bloque
    print('Tienes un gato')
elif mascota == 'perro':
    # ➡️ Si esta condición es verdadera, se ejecuta este bloque
    print('Tienes un perro')
elif mascota == 'pez':
    # ➡️ Si esta condición es verdadera, se ejecuta este bloque
    print('Tienes un pez')
else:
    # ➡️ Si ninguna condición anterior es verdadera, se ejecuta este bloque
    print('Tienes mascota?')
