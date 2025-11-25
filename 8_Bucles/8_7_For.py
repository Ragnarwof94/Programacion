#➡️ Recorriendo diccionarios con for
#➡️ Ejemplo de un ciclo for en Python
#➡️ La variable dato toma el valor de cada clave en el diccionario durante cada iteración del ciclo
#➡️ El ciclo for se repite hasta que se hayan recorrido todas las claves en el diccionario
#➡️ Inicialización del diccionario
diccionario = {1:'Uno',2:'Dos',3:'Tres'}
#➡️ Ciclo for para iterar sobre cada clave en el diccionario
#➡️ Imprime cada clave y su valor asociado
#➡️ Al finalizar el ciclo, se habrán impreso todas las claves y sus valores asociados en el diccionario
for dato in diccionario:
    #➡️ Imprime la clave actual y su valor asociado
    #➡️ La variable dato toma el valor de cada clave en el diccionario durante cada iteración del ciclo
    #➡️ El ciclo se repite hasta que se hayan recorrido todas las claves en el diccionario
    print(dato)

#➡️ Ciclo for para iterar sobre cada ítem (clave, valor) en el diccionario
#➡️ Imprime cada ítem (clave, valor)
#➡️ Al finalizar el ciclo, se habrán impreso todos los ítems (clave, valor) en el diccionario
for dato in diccionario.items():
    #➡️ Imprime el ítem (clave, valor) actual
    #➡️ La variable dato toma el valor de cada ítem (clave, valor) en el diccionario durante cada iteración del ciclo
    #➡️ El ciclo se repite hasta que se hayan recorrido todos los ítems (clave, valor) en el diccionario
    print(dato)

#➡️ Ciclo for para iterar sobre cada clave y valor en el diccionario
#➡️ Imprime cada valor y su clave asociada
#➡️ Al finalizar el ciclo, se habrán impreso todos los valores y sus claves asociadas en el diccionario
for clave, dato in diccionario.items():
    #➡️ Imprime el valor actual y su clave asociada
    #➡️ La variable dato toma el valor de cada valor en el diccionario durante cada iteración del ciclo
    print(dato)
    #➡️ Imprime la clave actual
    #➡️ La variable clave toma el valor de cada clave en el diccionario durante cada iteración del ciclo
    print(clave)

#➡️ Ciclo for para iterar sobre cada valor en el diccionario
#➡️ Imprime cada valor
for dato in diccionario.values():
    #➡️ Imprime el valor actual
    #➡️ La variable dato toma el valor de cada valor en el diccionario durante cada iteración del ciclo
    print(dato)

#➡️ Ciclo for para iterar sobre cada clave en el diccionario
#➡️ Imprime cada clave
for dato in diccionario.keys():
    #➡️ Imprime la clave actual
    #➡️ La variable dato toma el valor de cada clave en el diccionario durante cada iteración del ciclo
    print(dato)
