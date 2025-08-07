class Repartidor:
    def __init__(self, nombre,paquetes,zona):
        self.nombre=nombre
        self.paquetes=paquetes
        self.zona=zona

    def __str__(self):
        return (f"{self.nombre}, {self.paquetes},{self.zona}")
class Mensajeria:
    def __init__(self):
        self.repartidores=[]
    def agregarRepartidores(self,repartidor):
        self.repartidores.append(repartidor)

    def quick_sort(lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return quick_sort(menores) + iguales + quick_sort(mayores)



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