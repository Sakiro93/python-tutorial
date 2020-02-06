from articulos.CtrArticulo import ctrArticulo
from articulos.ModArticulo import modArticulo

ctr = ctrArticulo()

print('Insertar datos')

for i in range(3):
    descripcion = input('Ingrese descripcion: ')
    precio = input('Ingrese precio: ')
    stock = input('Ingrese stock: ')
    #art = modArticulo(0,descripcion,precio,stock)
    art=modArticulo(des=descripcion,pre=precio,sto=stock)
    if ctr.ingresar(art):
        print('Registro grabado correctamente')
    else:
        print('Error al grabar el Registro')


'''
print('Modificar datos')
for i in range(1):
    codigo = input('Ingrese codigo: ')
    descripcion = input('Ingrese descripcion: ')
    precio = input('Ingrese precio: ')
    stock = input('Ingrese stock: ')
    #art = modArticulo(0,descripcion,precio,stock)
    art=modArticulo(cod=codigo,des=descripcion,pre=precio,sto=stock)
    if ctr.modificar(art):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar el Registro')

'''
'''
print('Eliminar Datos')
codigo = input('Ingrese codigo: ')
art=modArticulo(cod=codigo)
if ctr.eliminar(art):
    print('Registro eliminado correctamente')
else:
    print('Error al eliminar el Registro')

articulos = ctr.consulta()
print('Codigo Descripcion Precio Stock')
for registro in articulos:
    print('{:4} {:13} {:5} {:7}'.format(registro[0],registro[1],registro[2],registro[3]))'''