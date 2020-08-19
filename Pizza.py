class Pizza:
    def __init__(self, nombre,ingredientes, tamanio,tipo,preciobase):
        self.nombre =nombre
        self.ingredientes =ingredientes
        self.tipo =tipo
        self.tamanio = tamanio
        self.preciobase = preciobase
        self.precio =self.__calcularPrecio()
    
    def __calcularPrecio(self):
        precio=0
        if self.tipo == 'piedra' :
            precio = self.tamanio*3*self.preciobase
        elif self.tipo == 'parrilla':
            precio= self.tamanio*2*self.preciobase
        else:
            precio=self.tamanio*1.5*self.preciobase
        return precio
    
#p = Pizza('muzza', ['queso', 'jamon'], 8, 'piedra')

#print(p.precio)