#➡️ Calcular el promedio de una lista de números
#➡️ Ejemplo de un ciclo for en Python
#➡️ Suma todos los números en la lista y luego divide por la cantidad de números para obtener el promedio
#➡️ La variable numero toma el valor de cada elemento en la lista durante cada iteración del ciclo
#➡️ El ciclo for se repite hasta que se hayan sumado todos los números en la lista
#➡️ Inicialización de la lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]
#➡️ Variable para almacenar la suma de los números
valor = 0
#➡️ Ciclo for para iterar sobre cada número en la lista
#➡️ Suma cada número a la variable valor
#➡️ Al finalizar el ciclo, la variable valor contendrá la suma de todos los números en la lista
for numero in numeros:
    #➡️ Suma el número actual a la variable valor
    #➡️ La variable numero toma el valor de cada elemento en la lista durante cada iteración
    #➡️ El ciclo se repite hasta que se hayan sumado todos los números en la lista
    #➡️ Al finalizar el ciclo, la variable valor contendrá la suma de todos los números en la lista
    #➡️ Suma el número actual a la variable valor
    valor = valor + numero
#➡️ Calcula el promedio dividiendo la suma total por la cantidad de números en la lista
#➡️ Imprime el promedio de los números en la lista
#➡️ La función len() devuelve la cantidad de elementos en la lista
#➡️ Imprime el resultado del promedio
print(valor/len(numeros))
