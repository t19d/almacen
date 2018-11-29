# encoding: utf-8
from sqlalchemy import *
from sqlalchemy import exc
#import sqlalchemy
import MySQLdb

# Propietario: David Tojo

###OBJETOS DE LA BASE DE DATOS###
#################################################################################################

class Cliente:
   def __init__(self, identificador, id_producto, nombre, apellidos, alias, dni, calle, portal, piso, localidad, provincia, pais,
                tel_movil, tel_trabajo, tel_altern, tel_casa, fax, email, n_cuenta, notas):
       self.identificador = identificador
       self.id_producto = id_producto
       self.nombre = nombre
       self.apellidos = apellidos
       self.alias = alias
       self.dni = dni
       self.calle = calle
       self.portal = portal
       self.piso = piso
       self.localidad = localidad
       self.provincia = provincia
       self.pais = pais
       self.tel_movil = tel_movil
       self.tel_trabajo = tel_trabajo
       self.tel_altern = tel_altern
       self.tel_casa = tel_casa
       self.fax = fax
       self.email = email
       self.n_cuenta = n_cuenta
       self.notas = notas


class Proveedor:
   def __init__(self, identificador, cif, razon, alias, actividad, calle, portal, piso, localidad, cp, provincia, pais,
                tel1, tel2, fax, pag_web, email, n_cuenta, persona_contacto1, persona_contacto2):
       self.identificador = identificador
       self.cif = cif
       self.razon = razon
       self.alias = alias
       self.actividad = actividad
       self.calle = calle
       self.portal = portal
       self.piso = piso
       self.localidad = localidad
       self.cp = cp
       self.provincia = provincia
       self.pais = pais
       self.tel1 = tel1
       self.tel2 = tel2
       self.fax = fax
       self.pag_web = pag_web
       self.email = email
       self.n_cuenta = n_cuenta
       self.persona_contacto1 = persona_contacto1
       self.persona_contacto2 = persona_contacto2


class Articulo:
   def __init__(self, identificador, codigo, descrip, pvp, unidades, stock_seg, stock_min, pm_coste, ult_pcoste):
       self.identificador = identificador
       self.codigo = codigo
       self.descrip = descrip
       self.pvp = pvp
       self.unidades = unidades
       self.stock_seg = stock_seg
       self.stock_min = stock_min
       self.pm_coste = pm_coste
       self.ult_pcoste = ult_pcoste

   def calcularPM_Coste(self, p_coste, existencias_iniciales, existencias_entrantes):
       self.pm_coste = ((existencias_iniciales * self.pm_coste) + (existencias_entrantes * p_coste)) / (
               existencias_iniciales + existencias_entrantes)

#################################################################################################

###CONEXION BASE DATOS###
#################################################################################################
class connection:
    def __init__(self, usuario='root', passwd='abc123.', hst='localhost', db='almacen'):
####CONEXION####
        self.usuario = usuario
        self.passwd = passwd
        self.host = hst
        self.database = db

        cad = 'mysql://' + self.usuario + ':' + self.passwd + '@' + self.host + '/' + self.database

        try:
            self.engine = create_engine(cad)
            self.con = self.engine.connect()
            self.engine.echo = False
            self.m = MetaData(self.engine)

        except exc.OperationalError:
            print('Error: ')

####TABLAS####
        #Creación de la variable tabla clientes:
        self.clientes = Table('clientes', self.m,
                                  Column('idCliente', Integer, primary_key=True, autoincrement=true),
                                  Column('idProducto', Integer), Column('nombre', String(40)),
                                  Column('apellidos', String(40)), Column('alias', String(40)),
                                  Column('dni', String(9)), Column('calle', String(25)), Column('portal', String(4)),
                                  Column('piso', String(2)), Column('localidad', String(40)),
                                  Column('provincia', String(25)), Column('pais', String(25)),
                                  Column('telCasa', String(10)), Column('telMovil', String(10)),
                                  Column('telTrabajo', String(10)), Column('telAlternativo', String(10)),
                                  Column('fax', String(10)), Column('email', String(40)),
                                  Column('numeroCuenta', String(12)), Column('notas', String(50)))
        #Creación de la tabla clientes si no existe:
        if  not self.clientes.exists():
            self.clientes.create()

        #Creación de la variable tabla proveedores:
        self.proveedores = Table('proveedores', self.m,
                                     Column('idProveedor', Integer, primary_key=True, autoincrement=True),
                                     Column('cif', String(10)), Column('razon', String(40)),
                                     Column('alias', String(40)), Column('actividad', String(30)),
                                     Column('calle', String(25)), Column('portal', String(4)),
                                     Column('piso', String(2)), Column('localidad', String(40)),
                                     Column('cp', String(5)), Column('provincia', String(25)),
                                     Column('pais', String(25)), Column('tel1', String(10)), Column('tel2', String(10)),
                                     Column('fax', String(10)), Column('pagweb', String(40)),
                                     Column('email', String(40)), Column('numeroCuenta', String(12)),
                                     Column('personaContacto1', String(40)), Column('personaContacto2', String(40)))
        #Creación de la tabla proveedores si no existe:
        if  not self.proveedores.exists():
            self.proveedores.create()


        #Creación de la variable tabla articulos:
        self.articulos = Table('articulos', self.m,
                                   Column('idArticulo', Integer, primary_key=True, autoincrement=True),
                                   Column('codigo', String(8)), Column('descrip', String(30)), Column('pvp', Integer),
                                   Column('unidades', Integer), Column('stockSeg', Integer),
                                   Column('stockMin', Integer), Column('pmCoste', Integer),
                                   Column('ultPCoste', Integer))
        #Creación de la tabla articulos si no existe:
        if  not self.articulos.exists():
            self.articulos.create()
#################################################################################################

###CLIENTES###
#################################################################################################

    def insertarCliente(self, c, n):
        #Insertar cliente:
        ins = self.clientes.insert()
        ins.execute(idCliente = str(n+1),idProducto=c.id_producto, nombre=c.nombre, apellidos=c.apellidos, alias=c.alias, dni=c.dni, calle=c.calle, portal=c.portal, piso=c.piso, localidad=c.localidad, provincia=c.provincia, pais=c.pais, telCasa=c.tel_casa, telMovil=c.tel_movil, telTrabajo=c.tel_trabajo, telAlternativo=c.tel_altern, fax=c.fax, email=c.email, numeroCuenta=c.n_cuenta, notas=c.notas)

    def consultarCliente(self):
        # Consultar datos:
        rs = self.con.execute('SELECT * FROM clientes')
        # Devolver lista de clientes:
        listaClientes = []
        for a in rs:
            client = Cliente(a.idCliente, a.idProducto, a.nombre, a.apellidos, a.alias, a.dni, a.calle, a.portal, a.piso,
                             a.localidad, a.provincia, a.pais, a.telCasa, a.telMovil, a.telTrabajo, a.telAlternativo,
                             a.fax, a.email, a.numeroCuenta, a.notas)
            listaClientes.append(client)
        return listaClientes

    def eliminarCliente(self, c):
        #Eliminar el registro:
        self.con.execute("DELETE FROM `clientes` WHERE `idCliente`='%s'"% (str(c.identificador)))

    def modificarCliente(self, c):
        #Primero se elimina el registro:
        self.con.execute("DELETE FROM `clientes` WHERE `idCliente`='%s'"% (str(c.identificador)))
        #Por último, se vuelve a crear el registro:
        ins = self.clientes.insert()
        ins.execute(idCliente = c.identificador, idProducto=c.id_producto, nombre=c.nombre, apellidos=c.apellidos, alias=c.alias, dni=c.dni, calle=c.calle, portal=c.portal, piso=c.piso, localidad=c.localidad, provincia=c.provincia, pais=c.pais, telCasa=c.tel_casa, telMovil=c.tel_movil, telTrabajo=c.tel_trabajo, telAlternativo=c.tel_altern, fax=c.fax, email=c.email, numeroCuenta=c.n_cuenta, notas=c.notas)

#################################################################################################

###PROVEEDORES###
#################################################################################################
    def insertarProveedor(self, p, n):
        #Insertar proveedor:
        ins = self.proveedores.insert()
        ins.execute(idProveedor = str(n+1), cif=p.cif, razon=p.razon, alias=p.alias, actividad=p.actividad, calle=p.calle, portal=p.portal, piso=p.piso, localidad=p.localidad, cp=p.cp, provincia=p.provincia, pais=p.pais, tel1=p.tel1, tel2=p.tel2, fax=p.fax, pagweb=p.pag_web, email=p.email, numeroCuenta=p.n_cuenta, personaContacto1=p.persona_contacto1, personaContacto2=p.persona_contacto2)

    def consultarProveedor(self):
        # Consultar datos:
        rs = self.con.execute('SELECT * FROM proveedores')
        # Devolver lista de proveedores:
        listaProveedores = []
        for a in rs:
            prov = Proveedor(a.idProveedor, a.cif, a.razon, a.alias, a.actividad, a.calle, a.portal, a.piso, a.localidad, a.cp,
                             a.provincia, a.pais, a.tel1, a.tel2, a.fax, a.pagweb, a.email, a.numeroCuenta,
                             a.personaContacto1, a.personaContacto2)
            listaProveedores.append(prov)
        return listaProveedores

    def eliminarProveedor(self, p):
        #Eliminar el registro:
        self.con.execute("DELETE FROM `proveedores` WHERE `idProveedor`='%s'"% (str(p.identificador)))

    def modificarProveedor(self, p):
        #Primero se elimina el registro:
        self.con.execute("DELETE FROM `proveedores` WHERE `idProveedor`='%s'"% (str(p.identificador)))
        #Por último, se vuelve a crear el registro:
        ins = self.proveedores.insert()
        ins.execute(idProveedor = p.identificador, cif=p.cif, razon=p.razon, alias=p.alias, actividad=p.actividad, calle=p.calle, portal=p.portal, piso=p.piso, localidad=p.localidad, cp=p.cp, provincia=p.provincia, pais=p.pais, tel1=p.tel1, tel2=p.tel2, fax=p.fax, pagweb=p.pag_web, email=p.email, numeroCuenta=p.n_cuenta, personaContacto1=p.persona_contacto1, personaContacto2=p.persona_contacto2)

#################################################################################################


###ARTICULOS###
#################################################################################################
    def insertarArticulo(self, art, n):
        #Insertar articulo:
        ins = self.articulos.insert()
        ins.execute(idProveedor = str(n+1),codigo=art.codigo, descrip=art.descrip, pvp=art.pvp, unidades=art.unidades, stockSeg=art.stock_seg, stockMin=art.stock_min, pmCoste=art.pm_coste, ultPCoste=art.ult_pcoste)

    def consultarArticulo(self):
        # Consultar datos:
        rs = self.con.execute('SELECT * FROM articulos')
        # Devolver lista de articulos:
        listaArticulos = []
        for a in rs:
            artic = Articulo(a.idArticulo, a.codigo, a.descrip, a.pvp, a.unidades, a.stockSeg, a.stockMin, a.pmCoste, a.ultPCoste)
            listaArticulos.append(artic)
        return listaArticulos

    def eliminarArticulo(self, a):
        #Eliminar el registro:
        self.con.execute("DELETE FROM `articulos` WHERE `idArticulo`='%s'"% (str(a.identificador)))


    def modificarArticulo(self, art):
        #Primero se elimina el registro:
        self.con.execute("DELETE FROM `articulos` WHERE `idArticulo`='%s'"% (str(art.identificador)))
        #Por último, se vuelve a crear el registro:
        ins = self.articulos.insert()
        ins.execute(idProveedor = art.identificador, codigo=art.codigo, descrip=art.descrip, pvp=art.pvp, unidades=art.unidades, stockSeg=art.stock_seg, stockMin=art.stock_min, pmCoste=art.pm_coste, ultPCoste=art.ult_pcoste)

#################################################################################################
