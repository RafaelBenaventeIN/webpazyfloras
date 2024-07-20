import pymysql
pymysql.install_as_MySQLdb()

import configparser
# Leer configuración desde el archivo database.ini
config = configparser.ConfigParser()
config.read('database.ini')

conn = pymysql.Connection(
    database=config['database']['NAME'],
    user=config['database']['USER'],
    passwd=config['database']['PASSWORD'])

curr = conn.cursor()

curr.execute('select * from tienda_producto')

productos = curr.fetchall()

for registro in productos:
    print(registro)


curr.execute('select * from tienda_servicio')

servicios = curr.fetchall()

for registro in servicios:
    print(registro)

mis_productos = [
(1, 'vasija', 'Vasija de barro Tetera', 16000, 'Vasija decorativa para patio trasero con forma de tetera.', 'productos/1.jpeg', 1),
(2, 'vasija', 'Vasija de Aluminio Gris', 36000, 'Vasija decorativa para interior del hogar, elegante pieza.', 'productos/2.jpeg', 1),
(3,	'vasija', 'Vasija de barro azteca', 10000, 'Vasija con forma de antigua civilización azteca.','productos/3.jpeg', 1),
(4, 'vasija', 'Vasija de barro jardín', 25000, 'Vasija decorativa de modelo básico para colocar plantas.', 'productos/4.jpeg', 1),

(5, 'macetero', 'Maceta de cerámica Eiffell', 8000, 'Pequeña maceta decorativa con torre Eiffell y bicicleta.', 'productos/5.jpeg', 1),
(6, 'macetero', 'Maceta de cerámica Love', 8000, 'Pequeña maceta de mesa con figura de corazón y letras LOVE.', 'productos/6.jpeg', 1),
(7, 'macetero', 'Maceta de vidrio', 10000, 'Maceta de regalo con cuarzo y conchita decorativa.', 'productos/7.jpeg', 1),
(8, 'macetero', 'Maceta de loza', 8000, 'Pequeña maceta de loza blanca en base a figuras geométricas.', 'productos/8.jpeg', 1),

(9, 'planta', 'Orquídea Mariposa', 4000, 'Variedad que se adapta muy bien la vida de interiores para ganar altura y luz.', 'productos/9.jpeg', 1),
(10, 'planta', 'Margarita Livingstone', 3000, 'Planta de pétalos de colores variados con un bajo costo de mantenimiento.', 'productos/10.jpeg', 1),
(11, 'planta', 'Aloe Vera', 14000, 'Mundialmente reconocida por sus usos y propiedades por lo que tiene un gran valor económico.', 'productos/11.jpeg', 1),
(12, 'planta', 'Llama Roja', 5000, 'Considerada como una especie geométricamente perfecta. Su perfección se contempla durante el verano.', 'productos/12.jpeg', 1)
]

mis_servicios = [
    (1, 'Murallismo', 72000, 'Puede tener uno de estos cuadros vivos en el lugar que guste.', 'servicios/1.png', 1)
]

productos_a_agregar = []


for mi_producto in mis_productos:
    producto_existe = False
    for producto in productos:
        if mi_producto[0]==producto[0]:
            producto_existe = True
            break
    if not producto_existe:
        productos_a_agregar.append(tuple(mi_producto[:]))

for product in productos_a_agregar:
    print(product[0])

for producto_a_agregar in productos_a_agregar:
    print(producto_a_agregar)
    producto_values = "("+str(producto_a_agregar[0])+", "
    producto_values += "'"+str(producto_a_agregar[1])+"', "
    producto_values += "'"+str(producto_a_agregar[2])+"', "
    producto_values += "'"+str(producto_a_agregar[3])+"', "
    producto_values += "'"+str(producto_a_agregar[4])+"', "
    producto_values += "'"+str(producto_a_agregar[5])+"', "
    producto_values +=  ""+str(producto_a_agregar[6])+")"

    sqlinsert = "insert into tienda_producto (id, tipo, nombre, precio, descripcion, imagen, activo) values"+ producto_values
    print(sqlinsert)
    curr.execute(sqlinsert)
    conn.commit()

servicios_a_agregar = []


for mi_servicio in mis_servicios:
    servicio_existe = False
    for servicio in servicios:
        if mi_servicio[0]==servicio[0]:
            servicio_existe = True
            break
    if not servicio_existe:
        servicios_a_agregar.append(tuple(mi_servicio[:]))

for service in servicios_a_agregar:
    print(service[0])

for servicio_a_agregar in servicios_a_agregar:
    print(servicio_a_agregar)
    servicio_values = "("+str(servicio_a_agregar[0])+", "
    servicio_values += "'"+str(servicio_a_agregar[1])+"', "
    servicio_values += "'"+str(servicio_a_agregar[2])+"', "
    servicio_values += "'"+str(servicio_a_agregar[3])+"', "
    servicio_values += "'"+str(servicio_a_agregar[4])+"', "
    servicio_values += "'"+str(servicio_a_agregar[5])+"') "

    sqlinsert = "insert into tienda_servicio (id, nombre, precio, descripcion, imagen, activo) values"+ servicio_values
    print(sqlinsert)
    curr.execute(sqlinsert)
    conn.commit()
