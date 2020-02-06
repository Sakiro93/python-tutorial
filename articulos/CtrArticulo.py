from articulos.DaoArticulo import daoArticulo

class ctrArticulo:
    def __init__(self, art=None):
        self.articulo = art

    def consulta(self):
        objDao = daoArticulo()
        return objDao.consultar()

    def ingresar(self, art):
        objDao = daoArticulo()
        return objDao.ingresar(art)

    def modificar(self, art):
        objDao = daoArticulo()
        return objDao.modificar(art)

    def eliminar(self, art):
        objDao = daoArticulo()
        return objDao.eliminar(art)