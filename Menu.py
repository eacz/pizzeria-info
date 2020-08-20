class Menu:
    def __init__(self, pizzas):
        self.pizzas=pizzas
    
    def agregarPizza(self, pizza):
        self.pizzas.append(pizza)

    def mostrarMenu(self):
        for pizza in self.pizzas:
            print(f'La pizza {pizza.nombre} con los ingredientes {self.__listarIngredientes(pizza)} tiene el precio de {pizza.precio} con el tamaño de {pizza.tamanio} porciones, y el tipo es {pizza.tipo}')

            

    def __listarIngredientes(self,pizza):
        ingredientes = ''
        for i in range(len(pizza.ingredientes)):
            ingredientes+= str(pizza.ingredientes[i]) + ', '
        return ingredientes