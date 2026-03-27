def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("Precio: "))
    print(f'Precio: {precio}')
    descuento = float(input('Descuento: '))
    print(f'Descuento: {descuento}')
    precio_descuento = precio - descuento
    print(f'Precio con descuento: {precio_descuento}')
    cantidad = int(input())
    print(f'Total: {cantidad * precio_descuento}')
