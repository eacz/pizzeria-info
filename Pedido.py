import datetime
class Pedido:
    def __init__(self,pizzas, cliente, tiempo, fecha=datetime.datetime.now()):
        self.pizzas=pizzas
        self.cliente = cliente
        self.tiempo=tiempo
        self.precioTotal= self.__calcularPrecioTotal()
        self.fecha=fecha
        
    def __calcularPrecioTotal(self):
        precio = 0
        for p in self.pizzas:
            precio+= p['pizza'].precio*p['cantidad']
        return precio
        
    def pedidoListo(self):
        print(f'Despues de {self.tiempo} minutos el pedido de {len(self.pizzas)} pizzas de {self.cliente.getNombre} esta listo')
        print(f'Seran {self.precioTotal}$')
        
    def mostrarPedido(self):
        print('Las pizzas son: ')
        for i in range(len(self.pizzas)):
            print(self.pizzas[i]['pizza'])
            print(f"Cantidad: {self.pizzas[i]['cantidad']}")
            print('\n')
        print(f'El cliente es {self.cliente.getNombre()}')
        print(f'El precio a pagar del pedido es de: {self.precioTotal}')
        print(f'Y el estara listo en: {self.tiempo} minutos')
            