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
menu.mostrarMenu()



pizzas=[]
while True:
    pizza = int(input('Pizza: '))
    cantidad = int(input('Cantidad: '))
    pedido = {'pizza': menu.pizzas[pizza-1], 'cantidad': cantidad}
    pizzas.append(pedido)
    pregunta = input('Quiere realizar otro pedido? si/no ')
    if pregunta.lower() == 'no':
        break;
    
tiempo = int(input('Cuanto tiempo estima que va tardar? (en minutos) '))

p = Pedido(pizzas, c, tiempo, datetime.datetime(2020, 18, 15))
print(f'El precio sera de {p.precioTotal}')
p.pedidoListo()
    
    
    
