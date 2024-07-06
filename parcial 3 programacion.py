import json
from tabulate import tabulate
class Pedido:
    def __init__(self, nombre, apellido, contacto, tipo_evento, fecha, direccion, menu, cantidad_comensales):
        self.nombre = nombre
        self.apellido = apellido
        self.contacto = contacto
        self.tipo_evento = tipo_evento
        self.fecha = fecha
        self.direccion = direccion
        self.menu = menu
        self.cantidad_comensales = cantidad_comensales

    def to_dict(self):
        return {
            'Nombre': self.nombre,
            'Apellido': self.apellido,
            'Contacto': self.contacto,
            'Tipo de Evento': self.tipo_evento,
            'Fecha': self.fecha,
            'Dirección': self.direccion,
            'Menú': self.menu,
            'Cantidad de Comensales': self.cantidad_comensales
        }

def registrar_pedido():
    print("Registro de Nuevo Pedido\n")
    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    contacto = input("Número de contacto: ")
    tipo_evento = input("Tipo de evento (corporativo / privado): ")
    fecha = input("Fecha del evento (YYYY-MM-DD): ")
    direccion = input("Dirección del evento: ")

    print("\nSeleccione el menú:")
    print("1. Comida Italiana")
    print("2. Comida Japonesa")
    print("3. BBQ")
    opcion_menu = input("Ingrese el número correspondiente al menú seleccionado: ")

    menus = {
        '1': 'Comida Italiana',
        '2': 'Comida Japonesa',
        '3': 'BBQ'
    }

    if opcion_menu not in menus:
        print("Opción de menú inválida.")
        return

    menu_seleccionado = menus[opcion_menu]
    cantidad_comensales = int(input("Cantidad de comensales: "))

    pedido = Pedido(nombre, apellido, contacto, tipo_evento, fecha, direccion, menu_seleccionado, cantidad_comensales)

    # Guardar pedido en archivo de texto (.txt)
    with open(f"pedido_{menu_seleccionado.lower().replace(' ', '_')}.txt", 'a') as file_txt:
        file_txt.write(str(pedido) + "\n\n")

    # Guardar pedido en archivo JSON (.json)
    with open(f"pedido_{menu_seleccionado.lower().replace(' ', '_')}.json", 'a') as file_json:
        json.dump(pedido.to_dict(), file_json, indent=4)
        file_json.write("\n")

    print("\nPedido registrado correctamente!\n")

def mostrar_tabla_pedidos():
    # Mostrar una tabla al final con los pedidos registrados
    headers = ['Nombre', 'Apellido', 'Contacto', 'Tipo de Evento', 'Fecha', 'Dirección', 'Menú', 'Cantidad de Comensales']
    tabla_pedidos = []

    # Leer los archivos .json para construir la tabla
    menus = ['comida_italiana', 'comida_japonesa', 'bbq']
    for menu in menus:
        try:
            with open(f"pedido_{menu}.json", 'r') as file_json:
                data = json.load(file_json)
                tabla_pedidos.append([data[key] for key in headers])
        except FileNotFoundError:
            continue

    # Imprimir tabla usando tabulate
    if tabla_pedidos:
        print("\nTabla de Pedidos Registrados\n")
        print(tabulate(tabla_pedidos, headers=headers, tablefmt="grid"))
    else:
        print("\nAún no se han registrado pedidos.\n")

def main():
    while True:
        print("\nBienvenido a Gourmet Services - Sistema de Gestión de Pedidos\n")
        print("1. Registrar Pedido")
        print("2. Mostrar Tabla de Pedidos")
        print("3. Salir del Programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            mostrar_tabla_pedidos()
        elif opcion == '3':
            print("\nGracias por usar nuestro sistema. ¡Hasta luego!\n")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
