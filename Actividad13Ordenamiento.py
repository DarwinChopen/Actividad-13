while True:
    print("Menu")
    print("1. Ingresar")
    print("2. Mostar")
    print("3. Ordenar")
    print("4. Estadisticas")
    print("5. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Opcion Invalida Ingrese otra")
    match opcion:
        case 1:
            print("Ingreso Repartidores")
        case 2:
            print("Mostrar ")
        case 3:
            print("Ordenarlos")
        case 4:
            print("Estadisticas")
        case 5:
            print("Salir")
            break
        case _:
            print("Opcion Invalida")