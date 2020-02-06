class modArticulo:
    def __init__(self, cod=1, des='', pre=0, sto=0):
        self.__codigo = cod
        self.__descripcion = des
        self.__precio = pre
        self.__stock = sto

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, cod):
        self.__codigo = cod

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, des):
        self.__descripcion = des

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, pre):
        self.__precio = pre

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, sto):
        self.__stock = sto
