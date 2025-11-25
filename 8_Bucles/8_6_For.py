#➡️ Bucles For anidados
#➡️ Recorriendo listas de listas
#➡️ Ejemplo de un ciclo for anidado en Python
#➡️ La variable lista toma el valor de cada sublista en la lista principal durante cada iteración del ciclo externo
#➡️ La variable dato toma el valor de cada elemento en la sublista durante cada iteración del ciclo interno
#➡️ El ciclo for externo se repite hasta que se hayan recorrido todas las sublistas en la lista principal
#➡️ El ciclo for interno se repite hasta que se hayan recorrido todos los elementos en la sublista actual
#➡️ Inicialización de la lista de listas
listas = [[1,2],[3,4],[5,6]]
#➡️ Ciclo for externo para iterar sobre cada sublista en la lista principal
#➡️ Ciclo for interno para iterar sobre cada elemento en la sublista actual

for lista, dato in listas:
    #➡️ Imprime la sublista actual y el elemento actual
    #➡️ La variable lista toma el valor de cada sublista en la lista principal durante cada iteración del ciclo externo
    #➡️ La variable dato toma el valor de cada elemento en la sublista durante cada iteración del ciclo interno
    print(lista)
    #➡️ Imprime el elemento actual
    #➡️ La variable dato toma el valor de cada elemento en la sublista durante cada iteración del ciclo interno
    #➡️ La variable dato toma el valor de cada elemento en la sublista durante cada iteración del ciclo interno
    print(dato)
