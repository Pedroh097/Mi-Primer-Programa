
salida = False
agenda = dict()
while not salida:
    accion = input("¿Que Quieres Hacer? (Añadir numero [A] / Consultar numero [C] / Salir [S]:)")
    #Accion añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        print("-------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero


    #Accion consultar
    elif accion == "C":
       print("Vamos a consultar un numero:")
       print("-------------------------------------")
       numero = input("De quien quieres saber el numero:")
       print(agenda[nombre])


    # Accion salir
    elif accion == "S":
        salida = True