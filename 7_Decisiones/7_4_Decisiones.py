#➡️ Decisiones Anidadas
#➡️  Ejemplo de decisiones anidadas en Python
#➡️  Verifica si una persona es mayor de edad y si tiene suficiente dinero para entrar a un club
#➡️ Si la persona es menor de edad, imprime "Menor de edad"
#➡️ Si la persona es mayor de edad y tiene más de 9000 en dinero, imprime "Puede entrar"
#➡️ Si la persona es mayor de edad pero no tiene suficiente dinero, imprime "No puede entrar"
#➡️ Edad de la persona
edad = 19
#➡️ Cantidad de dinero disponible
dinero = 10000
#➡️ Decisión anidada
#➡️ Verifica si es menor o mayor de edad
#➡️ Si es mayor de edad, verifica la cantidad de dinero
#➡️ Imprime el resultado correspondiente
if edad < 18:
    #➡️ Si es menor de edad
    print("Menor de edad")
else:
    #➡️ Si es mayor de edad
    print("Mayor de edad")
    #➡️ Verifica la cantidad de dinero
    if dinero > 9000:
        #➡️ Si tiene suficiente dinero
        print("Puede entrar")
    else:
        #➡️ Si no tiene suficiente dinero
        print("No puede entrar")
