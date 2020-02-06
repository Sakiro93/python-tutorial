from conexion import Conector
class daoArticulo(Conector):
    def __init__(self, server='localhost', usuario='root', password='', basedato='inventario'):
        Conector.__init__(self, server='localhost', usuario='root', password='', basedato='inventario')

    def consultar(self):
        result = False
        try:
            sql = 'Select codigo id, descripcion des, precio pre, stock sto From articulo'
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, art):
        correcto = True
        try:
            sql = 'insert into articulo (descripcion, precio, stock) values (%s,%s,%s)'
            self.conectar()
            self.conector.execute(sql, (art.descripcion, art.precio, art.stock))
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, art):
        correcto = True
        try:
            sql = 'Update articulo set descripcion  = %s, precio  = %s , stock = %s where codigo = %s'
            self.conectar()
            self.conector.execute(sql, (art.descripcion, art.precio, art.stock, art.codigo))
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, art):
        correcto = True
        try:
            sql = 'delete from articulo where codigo = %s'
            self.conectar()
            self.conector.execute(sql, (art.codigo))
            self.conn.commit()
        except:
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto