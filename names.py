def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("Escribe tu nombre: ")
    apellido = input("Esribe tu apellido: ")
    nombre_minuscula = nombre.lower() + " " + apellido.lower()
    nombre_titulo = nombre.title() + " " + apellido.title()
    nombre_mayuscula = nombre.upper() + " " + apellido.upper()
    nombre_minuscula_tabulado = "\t" + nombre_minuscula

    print(nombre_minuscula)
    print(nombre_titulo)
    print(nombre_mayuscula)
    print(nombre_minuscula_tabulado)
