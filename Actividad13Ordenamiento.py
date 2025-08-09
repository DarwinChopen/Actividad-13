class Repartidor:
    def __init__(self, nombre,paquetes,zona):
        self.nombre=nombre
        self.paquetes=paquetes
        self.zona=zona

    def __str__(self):
        return (f"{self.nombre}, {self.paquetes},{self.zona}")

class Mensajeria:
    def __init__(self):
        self.repartidores={}
    def agregarRepartidores(self,repartidor):
        self.repartidores[repartidor.nombre]=repartidor

    def quick_sort(self,lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return self.quick_sort(mayores) + iguales + self.quick_sort(menores)

    def buscar(self,nombreObjetivo):
        for datos in self.repartidores.values():
            if datos.nombre==nombreObjetivo:
                return datos
        return  None


empresa=Mensajeria()
while True:
    print("Menu")
    print("1. Ingresar")
    print("2. Mostar")
    print("3. Ordenar")
    print("4 .Buscar")
    print("5. Estadisticas")
    print("6. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Opcion Invalida Ingrese otra")
    match opcion:
        case 1:
            print("Ingreso Repartidores")
            nombre = input("Nombre del Repartidor: ")
            try:
                paquetes = int(input("Cantidad de paquetes entregados: "))
            except ValueError:
                print("Ingrese un entero.")
                continue
            zona = input("Zona: ")
            empresa.agregarRepartidores(Repartidor(nombre, paquetes, zona))
        case 2:
            print("Mostrar ")
            if not empresa.repartidores:
                print("No hay repartidores registrados.")
            else:
                print("Lisatodo original")
                for var in empresa.repartidores.values():
                    print(var)
        case 3:
            print("Ordenarlos por paquetes")
            listaTemporal = [(var.paquetes, var.nombre, var.zona) for var in empresa.repartidores.values()]
            paquetesOrdenados = empresa.quick_sort(listaTemporal)
            for paquetes,nombre,zona in paquetesOrdenados:
                    print(f"Nombre: {nombre}")
                    print(f"Paquetes: {paquetes}")
                    print(f"Zona: {zona}")
                    print("_________________________")
        case 4:
            print("Buscar")
            nombreBbuscar = input("Ingrese el nombre del repartidor: ").strip()
            resultado = empresa.buscar(nombreBbuscar)
            if resultado:
                print(f"Nombre: {resultado.nombre}")
                print(f"Paquetes: {resultado.paquetes}")
                print(f"Zona: {resultado.zona}")
                print("_________________________")
            else:
                print("no se encontro a nadie.")
        case 5:
            print("Estadisticas")
        case 6:
            print("Salir")
            break
        case _:
            print("Opcion Invalida")