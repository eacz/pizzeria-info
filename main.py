import datetime

from Cliente import Cliente
from Pedido import Pedido
from Menu import Menu
from Pizza import Pizza

p1 = Pizza('muzza', ['queso', 'jamon'], 8, 'piedra',50)
p2 = Pizza('4 quesos', ['queso1', 'queso2', 'queso3', 'queso4'], 10, 'piedra',60)
p3 = Pizza('solo queso', ['mucho queso', 'masa'], 12, 'parrilla', 30)

c = Cliente('Juan')

menu = Menu([p1,p2])
menu.agregarPizza(p3)
pedidos=[]

def agregarPizza(menu):
        nombre=input('Ingrese el nombre de la pizza: ')
        print('Ingrese los ingredientes')
        ingredientes= []
        while True:
            ingrediente=input('Ingrese el ingrediente')
            ingredientes.append(ingrediente)
            otra=input('Desea agregar otro ingrediente? si/no ')
            if otra.lower() == 'no':
                break
        tamanio=int(input('Ingrese el tamaño de la pizza en porciones (8 - 10 - 12) '))
        tipo=input('Ingrese el tipo de la pizza (piedra - parrilla - horno) ').lower()
        preciobase=int(input('Ingrese el precio base: '))
        nuevaPizza = Pizza(nombre,ingredientes,tamanio,tipo,preciobase)
        menu.agregarPizza(nuevaPizza)
        
def hacerPedido(pedidos):
    pizzas=[]
    while True:
        pizza = int(input('Pizza: '))
        cantidad = int(input('Cantidad: '))
        pedido = {'pizza': menu.pizzas[pizza-1], 'cantidad': cantidad}
        pizzas.append(pedido)
        pregunta = input('Quiere pedir otra pizza? si/no ')
        if pregunta.lower() == 'no':
            break;
    tiempo = int(input('Cuanto tiempo estima que va tardar? (en minutos) '))
    nombreCliente = input('Ingrese el nombre del cliente: ')
    cliente = Cliente(nombreCliente)
    p = Pedido(pizzas, cliente, tiempo, datetime.datetime.now())
    pedidos.append(p)
    print(f'El precio sera de {p.precioTotal}')
    
def mostrarPedido(pedidos):
    print(f'Que pedido desea ver? 1 - {len(pedidos)}')
    opcionPedido=int(input())
    pedidos[opcionPedido-1].mostrarPedido()
    

def menuMain():
    print('Bienvenido! Que desea hacer? 1-Mostrar menu 2-Agregar una pizza al menu 3-Hacer un pedido 4-Mostrar pedidos 5-cerrar sistema')
    while True:
        opcion = int(input('Elija una opcion: '))
        if opcion == 1:
            menu.mostrarMenu()
        elif opcion == 2 :
            agregarPizza(menu)
        elif opcion == 3:
            hacerPedido(pedidos)
        elif opcion == 4:
            mostrarPedido(pedidos)
        elif opcion == 5:
            break;
        else:
            print('Opcion invalida')
        print('Que desea hacer? 1-Mostrar menu 2-Agregar una pizza al menu 3-Hacer un pedido 4-Mostrar pedidos 5-cerrar sistema')
        

menuMain()

    
    
    
