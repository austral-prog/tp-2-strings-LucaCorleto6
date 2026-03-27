def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    # - Inputs
    nombre_completo = input().lower()
    email = input().lower()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    # - Funciones

    nombre_limpio = nombre_completo.strip().title()
    espacio_nombre = nombre_limpio.find(" ")
    solo_nombre = nombre_limpio[:espacio_nombre]
    apellido = nombre_limpio[espacio_nombre+1:]
    dominio = email[email.find("@")+1:]
    suma = nota1 + nota2 + nota3
    promedio = suma/3

    # - Prints
    print("=" * 24)
    print('    FICHA DEL ALUMNO')
    print("=" * 24)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {nombre_limpio[0]}{nombre_limpio[(espacio_nombre + 1)]}")
    print(f"Usuario: {apellido.lower()}.{solo_nombre.lower()}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_limpio.replace(" ","_")}")
    print(f"Cantidad de a: {nombre_limpio.count("a")}")
    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {float(promedio)}")
    print(f"Promedio entero: {int(promedio)}")
    print("=" * 24)

