def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    
    print("Ingresar gasto:")
    gasto = float(input())
    print(round(gasto, 2))
    print("Dinero recibido")
    recibido = int(input())
    print(recibido)
    print("\nVuelto\n")

    pesos = int(recibido - gasto)
    centavos = round(((recibido - gasto) - pesos) * 100)

    print("Pesos:\n" + str(pesos))
    print("Centavos:\n" + str(centavos))

