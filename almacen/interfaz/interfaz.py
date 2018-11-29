#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade
import sys
sys.path.append('./db')
from basedatos import *
import commands
# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.Center()
        self.label_titulo_principal = wx.StaticText(self, wx.ID_ANY, (u"SELECCIONE UNA OPCI\u00d3N:"))
        self.button_clientes_principal = wx.Button(self, wx.ID_ANY, ("Clientes"))
        self.button_proveedores_principal = wx.Button(self, wx.ID_ANY, ("Proveedores"))
        self.button_articulos_principal = wx.Button(self, wx.ID_ANY, (u"Art\u00edculos"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_button_clientes_principal, self.button_clientes_principal)
        self.Bind(wx.EVT_BUTTON, self.on_button_proveedores_principal, self.button_proveedores_principal)
        self.Bind(wx.EVT_BUTTON, self.on_button_articulos_principal, self.button_articulos_principal)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle((u"Alamc\u00e9n"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.label_titulo_principal, 0, 0, 0)
        sizer_2.Add(self.button_clientes_principal, 0, 0, 0)
        sizer_2.Add(self.button_proveedores_principal, 0, 0, 0)
        sizer_2.Add(self.button_articulos_principal, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def on_button_clientes_principal(self, event):  # wxGlade: Principal.<event_handler>
        print "Cambiar a Clientes..."
        commands.getoutput('./. interfaz.py')
        self.frame1=Clientes(None, wx.ID_ANY, "")
        self.frame1.Show()
        self.Close()
        event.Skip()

    def on_button_proveedores_principal(self, event):  # wxGlade: Principal.<event_handler>
        print "Cambiar a Proveedores..."
        commands.getoutput('./. interfaz.py')
        self.frame1=Proveedores(None, wx.ID_ANY, "")
        self.frame1.Show()
        self.Close()
        event.Skip()

    def on_button_articulos_principal(self, event):  # wxGlade: Principal.<event_handler>
        print "Cambiar a Articulos..."
        commands.getoutput('./. interfaz.py')
        self.frame1=Articulos(None, wx.ID_ANY, "")
        self.frame1.Show()
        self.Close()
        event.Skip()

# end of class Principal

class Clientes(wx.Frame):
    def __init__(self, *args, **kwds):
        self.operacion = 0
        self.con=connection()
        self.lista = self.con.consultarCliente()
        self.pos = 0
        self.clienteVariacion = self.lista[0]
        self.ultimo = len(self.lista)+1
        # begin wxGlade: Clientes.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.Center()
        # Menu Bar
        self.clientes_menubar = wx.MenuBar()
        self.name_editar_cliente = wx.Menu()
        self.name_eliminar_cliente = wx.MenuItem(self.name_editar_cliente, 101, ("Eliminar..."), ("Eliminar cliente"), wx.ITEM_NORMAL)
        self.name_editar_cliente.AppendItem(self.name_eliminar_cliente)
        self.name_modificar_cliente = wx.MenuItem(self.name_editar_cliente, 102, ("Modificar..."), (u"Modificar informaci\u00f3n de un cliente"), wx.ITEM_NORMAL)
        self.name_editar_cliente.AppendItem(self.name_modificar_cliente)
        self.name_nuevo_cliente = wx.MenuItem(self.name_editar_cliente, 103, ("Nuevo..."), (u"A\u00f1adir un nuevo cliente"), wx.ITEM_NORMAL)
        self.name_editar_cliente.AppendItem(self.name_nuevo_cliente)
        self.clientes_menubar.Append(self.name_editar_cliente, ("Editar..."))
        self.SetMenuBar(self.clientes_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.clientes_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.clientes_toolbar)
        self.clientes_toolbar.AddLabelTool(104,("Primero"), wx.Bitmap("/home/td/BMPS/FRSREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Primer cliente"), ("Mostrar datos del primer cliente"))
        self.clientes_toolbar.AddLabelTool(105, ("Anterior"), wx.Bitmap("/home/td/BMPS/PRVREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Anterior cliente"), ("Mostrar datos del anterior cliente"))
        self.clientes_toolbar.AddLabelTool(106, ("Siguiente"), wx.Bitmap("/home/td/BMPS/NXTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Siguiente cliente"), ("Mostrar datos del siguiente cliente"))
        self.clientes_toolbar.AddLabelTool(107, (u"\u00daltimo"), wx.Bitmap("/home/td/BMPS/LSTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"\u00daltimo cliente"), (u"Mostrar datos del \u00faltimo cliente"))
        self.clientes_toolbar.AddLabelTool(108, ("Salir"), wx.Bitmap("/home/td/BMPS/CLOSE.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Salir de esta ventana"), (u"Volver al men\u00fa principal"))
        # Tool Bar end
        self.label_titulo_cliente = wx.StaticText(self, wx.ID_ANY, ("CLIENTES"))
        self.label_id_producto_cliente = wx.StaticText(self, wx.ID_ANY, ("Id producto"))
        self.text_ctrl_id_producto_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_nombre_cliente = wx.StaticText(self, wx.ID_ANY, ("Nombre"))
        self.text_ctrl_nombre_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_apellidos_cliente = wx.StaticText(self, wx.ID_ANY, ("Apellidos"))
        self.text_ctrl_apellidos_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_alias_cliente = wx.StaticText(self, wx.ID_ANY, ("Alias"))
        self.text_ctrl_alias_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_dni_cliente = wx.StaticText(self, wx.ID_ANY, ("DNI"))
        self.text_ctrl_dni_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_calle_cliente = wx.StaticText(self, wx.ID_ANY, ("Calle"))
        self.text_ctrl_calle_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_portal_cliente = wx.StaticText(self, wx.ID_ANY, ("Portal"))
        self.text_ctrl_portal_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_piso_cliente = wx.StaticText(self, wx.ID_ANY, ("Piso"))
        self.text_ctrl_piso_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_localidad_cliente = wx.StaticText(self, wx.ID_ANY, ("Localidad"))
        self.text_ctrl_localidad_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_provincia_cliente = wx.StaticText(self, wx.ID_ANY, ("Provincia"))
        self.text_ctrl_provincia_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_pais_cliente = wx.StaticText(self, wx.ID_ANY, (u"Pa\u00eds"))
        self.text_ctrl_pais_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_movil_cliente = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono m\u00f3vil"))
        self.text_ctrl_tel_movil_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_trabajo_cliente = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono trabajo"))
        self.text_ctrl_tel_trabajo_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_altern_cliente = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono alternativo"))
        self.text_ctrl_tel_altern_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_casa_cliente = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono casa"))
        self.text_ctrl_tel_casa_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_fax_cliente = wx.StaticText(self, wx.ID_ANY, ("Fax"))
        self.text_ctrl_fax_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_email_cliente = wx.StaticText(self, wx.ID_ANY, (u"Correo electr\u00f3nico"))
        self.text_ctrl_email_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_num_cuenta_cliente = wx.StaticText(self, wx.ID_ANY, (u"N\u00famero de cuenta"))
        self.text_ctrl_num_cuenta_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_notas_cliente = wx.StaticText(self, wx.ID_ANY, ("Notas"))
        self.text_ctrl_notas_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_empty_cliente = wx.StaticText(self, wx.ID_ANY, ("ID"))
        self.text_ctrl_empty_cliente = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_aceptar_cliente = wx.Button(self, wx.ID_ANY, ("ACEPTAR"))

        self.__set_properties()
        self.__do_layout()
        self.rellenarDatos()

        self.Bind(wx.EVT_MENU, self.eliminar_cliente, self.name_eliminar_cliente)
        self.Bind(wx.EVT_MENU, self.modificar_cliente, self.name_modificar_cliente)
        self.Bind(wx.EVT_MENU, self.nuevo_cliente, self.name_nuevo_cliente)
        self.Bind(wx.EVT_TOOL, self.primer_cliente, id=104)
        self.Bind(wx.EVT_TOOL, self.anterior_cliente, id=105)
        self.Bind(wx.EVT_TOOL, self.siguiente_cliente, id=106)
        self.Bind(wx.EVT_TOOL, self.ultimo_cliente, id=107)
        self.Bind(wx.EVT_TOOL, self.salir_cliente, id=108)
        self.Bind(wx.EVT_BUTTON, self.on_button_aceptar_cliente, self.button_aceptar_cliente)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Clientes.__set_properties
        self.SetTitle((u"Clientes - Almac\u00e9n"))
        self.clientes_toolbar.Realize()
        self.label_empty_cliente.Hide()
        self.text_ctrl_empty_cliente.Hide()
        self.button_aceptar_cliente.Disable()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Clientes.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(10, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(10, 2, 0, 0)
        sizer_3.Add(self.label_titulo_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_id_producto_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_id_producto_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_nombre_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_nombre_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_apellidos_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_apellidos_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_alias_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_alias_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_dni_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_dni_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_calle_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_calle_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_portal_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_portal_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_piso_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_piso_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_localidad_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_localidad_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.label_provincia_cliente, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_provincia_cliente, 0, 0, 0)
        sizer_4.Add(grid_sizer_1, 1, 0, 0)
        grid_sizer_2.Add(self.label_pais_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_pais_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_movil_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_movil_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_trabajo_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_trabajo_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_altern_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_altern_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_casa_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_casa_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_fax_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_fax_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_email_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_email_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_num_cuenta_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_num_cuenta_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_notas_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_notas_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.label_empty_cliente, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_empty_cliente, 0, 0, 0)
        sizer_4.Add(grid_sizer_2, 1, 0, 0)
        sizer_3.Add(sizer_4, 1, 0, 0)
        sizer_3.Add(self.button_aceptar_cliente, 0, 0, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade
    
    def rellenarDatos(self):
        self.text_ctrl_id_producto_cliente.AppendText(str(self.lista[self.pos].id_producto))
        self.text_ctrl_nombre_cliente.AppendText(str(self.lista[self.pos].nombre))
        self.text_ctrl_apellidos_cliente.AppendText(str(self.lista[self.pos].apellidos))
        self.text_ctrl_alias_cliente.AppendText(str(self.lista[self.pos].alias))
        self.text_ctrl_dni_cliente.AppendText(str(self.lista[self.pos].dni))
        self.text_ctrl_calle_cliente.AppendText(str(self.lista[self.pos].calle))
        self.text_ctrl_portal_cliente.AppendText(str(self.lista[self.pos].portal))
        self.text_ctrl_piso_cliente.AppendText(str(self.lista[self.pos].piso))
        self.text_ctrl_localidad_cliente.AppendText(str(self.lista[self.pos].localidad))
        self.text_ctrl_provincia_cliente.AppendText(str(self.lista[self.pos].provincia))
        self.text_ctrl_pais_cliente.AppendText(str(self.lista[self.pos].pais))
        self.text_ctrl_tel_movil_cliente.AppendText(str(self.lista[self.pos].tel_movil))
        self.text_ctrl_tel_trabajo_cliente.AppendText(str(self.lista[self.pos].tel_trabajo))
        self.text_ctrl_tel_altern_cliente.AppendText(str(self.lista[self.pos].tel_altern))
        self.text_ctrl_tel_casa_cliente.AppendText(str(self.lista[self.pos].tel_casa))
        self.text_ctrl_fax_cliente.AppendText(str(self.lista[self.pos].fax))
        self.text_ctrl_email_cliente.AppendText(str(self.lista[self.pos].email))
        self.text_ctrl_num_cuenta_cliente.AppendText(str(self.lista[self.pos].n_cuenta))
        self.text_ctrl_notas_cliente.AppendText(str(self.lista[self.pos].notas))
        self.text_ctrl_empty_cliente.AppendText(str(self.lista[self.pos].identificador))

    def limpiarDatos(self):
        self.text_ctrl_id_producto_cliente.SetValue('')
        self.text_ctrl_nombre_cliente.SetValue('')
        self.text_ctrl_apellidos_cliente.SetValue('')
        self.text_ctrl_alias_cliente.SetValue('')
        self.text_ctrl_dni_cliente.SetValue('')
        self.text_ctrl_calle_cliente.SetValue("")
        self.text_ctrl_portal_cliente.SetValue("")
        self.text_ctrl_piso_cliente.SetValue("")
        self.text_ctrl_localidad_cliente.SetValue("")
        self.text_ctrl_provincia_cliente.SetValue("")
        self.text_ctrl_pais_cliente.SetValue("")
        self.text_ctrl_tel_movil_cliente.SetValue("")
        self.text_ctrl_tel_trabajo_cliente.SetValue("")
        self.text_ctrl_tel_altern_cliente.SetValue("")
        self.text_ctrl_tel_casa_cliente.SetValue("")
        self.text_ctrl_fax_cliente.SetValue("")
        self.text_ctrl_email_cliente.SetValue("")
        self.text_ctrl_num_cuenta_cliente.SetValue("")
        self.text_ctrl_notas_cliente.SetValue("")
        self.text_ctrl_empty_cliente.SetValue("")

    def cambiarPrimerCliente(self):
        self.pos = 0
        self.limpiarDatos()
        self.rellenarDatos()

    def cambiarAnteriorCliente(self):
        if (self.pos > 0):
            self.pos = self.pos - 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarCliente(self):
        if (self.pos < len(self.lista)-1):
            self.pos = self.pos + 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarUltimoCliente(self):
        self.pos = len(self.lista)-1
        self.limpiarDatos()
        self.rellenarDatos()



    def crearClienteInsertar(self):
        self.clienteVariacion.identificador = self.ultimo
        self.clienteVariacion.id_producto = self.text_ctrl_id_producto_cliente.GetValue()
        self.clienteVariacion.nombre = self.text_ctrl_nombre_cliente.GetValue()
        self.clienteVariacion.apellidos = self.text_ctrl_apellidos_cliente.GetValue()
        self.clienteVariacion.alias = self.text_ctrl_alias_cliente.GetValue()
        self.clienteVariacion.dni = self.text_ctrl_dni_cliente.GetValue()
        self.clienteVariacion.calle = self.text_ctrl_calle_cliente.GetValue()
        self.clienteVariacion.portal = self.text_ctrl_portal_cliente.GetValue()
        self.clienteVariacion.piso = self.text_ctrl_piso_cliente.GetValue()
        self.clienteVariacion.localidad = self.text_ctrl_localidad_cliente.GetValue()
        self.clienteVariacion.provincia = self.text_ctrl_provincia_cliente.GetValue()
        self.clienteVariacion.pais = self.text_ctrl_pais_cliente.GetValue()
        self.clienteVariacion.tel_movil = self.text_ctrl_tel_movil_cliente.GetValue()
        self.clienteVariacion.tel_trabajo = self.text_ctrl_tel_trabajo_cliente.GetValue()
        self.clienteVariacion.tel_altern = self.text_ctrl_tel_altern_cliente.GetValue()
        self.clienteVariacion.tel_casa = self.text_ctrl_tel_casa_cliente.GetValue()
        self.clienteVariacion.fax = self.text_ctrl_fax_cliente.GetValue()
        self.clienteVariacion.email = self.text_ctrl_email_cliente.GetValue()
        self.clienteVariacion.n_cuenta = self.text_ctrl_num_cuenta_cliente.GetValue()
        self.clienteVariacion.notas = self.text_ctrl_notas_cliente.GetValue()


    def crearCliente(self):
        self.clienteVariacion.identificador = self.text_ctrl_empty_cliente.GetValue()
        self.clienteVariacion.id_producto = self.text_ctrl_id_producto_cliente.GetValue()
        self.clienteVariacion.nombre = self.text_ctrl_nombre_cliente.GetValue()
        self.clienteVariacion.apellidos = self.text_ctrl_apellidos_cliente.GetValue()
        self.clienteVariacion.alias = self.text_ctrl_alias_cliente.GetValue()
        self.clienteVariacion.dni = self.text_ctrl_dni_cliente.GetValue()
        self.clienteVariacion.calle = self.text_ctrl_calle_cliente.GetValue()
        self.clienteVariacion.portal = self.text_ctrl_portal_cliente.GetValue()
        self.clienteVariacion.piso = self.text_ctrl_piso_cliente.GetValue()
        self.clienteVariacion.localidad = self.text_ctrl_localidad_cliente.GetValue()
        self.clienteVariacion.provincia = self.text_ctrl_provincia_cliente.GetValue()
        self.clienteVariacion.pais = self.text_ctrl_pais_cliente.GetValue()
        self.clienteVariacion.tel_movil = self.text_ctrl_tel_movil_cliente.GetValue()
        self.clienteVariacion.tel_trabajo = self.text_ctrl_tel_trabajo_cliente.GetValue()
        self.clienteVariacion.tel_altern = self.text_ctrl_tel_altern_cliente.GetValue()
        self.clienteVariacion.tel_casa = self.text_ctrl_tel_casa_cliente.GetValue()
        self.clienteVariacion.fax = self.text_ctrl_fax_cliente.GetValue()
        self.clienteVariacion.email = self.text_ctrl_email_cliente.GetValue()
        self.clienteVariacion.n_cuenta = self.text_ctrl_num_cuenta_cliente.GetValue()
        self.clienteVariacion.notas = self.text_ctrl_notas_cliente.GetValue()

    def eliminar_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        
        self.crearCliente()
        self.con.eliminarCliente(self.clienteVariacion)
        self.lista = self.con.consultarCliente()
        self.limpiarDatos()
        self.pos=0
        self.rellenarDatos()
        print "Eliminando registro..."
        event.Skip()

    def modificar_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.button_aceptar_cliente.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.operacion = 2
        print "Modificando registro..."
        event.Skip()

    def nuevo_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.button_aceptar_cliente.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.limpiarDatos()
        self.operacion=1
        print "Anhadiendo registro..."
        event.Skip()

    def primer_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.cambiarPrimerCliente()
        event.Skip()

    def anterior_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.cambiarAnteriorCliente()
        event.Skip()

    def siguiente_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.cambiarCliente()
        event.Skip()

    def ultimo_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        self.cambiarUltimoCliente()
        event.Skip()

    def salir_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        print "Volviendo a la página principal..."
        commands.getoutput('./. interfaz.py')
        self.ventana=Principal(None, wx.ID_ANY, "")
        self.ventana.Show()
        self.Close()
        event.Skip()

    def on_button_aceptar_cliente(self, event):  # wxGlade: Clientes.<event_handler>
        #DESHABILITAR BOTÓN DESPUÉS DE HACER LA OPERACIÓN
        if (self.operacion == 1):
            self.crearClienteInsertar()
            self.con.insertarCliente(self.clienteVariacion,self.ultimo)
            self.lista = self.con.consultarCliente()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        elif (self.operacion == 2):
            self.crearCliente()
            self.con.modificarCliente(self.clienteVariacion)
            self.lista = self.con.consultarCliente()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        print "Aplicando cambios..."
        self.button_aceptar_cliente.Disable()
        event.Skip()

# end of class Clientes

class Proveedores(wx.Frame):
    def __init__(self, *args, **kwds):
        self.operacion = 0
        self.con=connection()
        self.lista = self.con.consultarProveedor()
        self.pos = 0
        self.proveedorVariacion = self.lista[0]
        self.ultimo = len(self.lista)+1
        # begin wxGlade: Proveedores.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.Center()
        # Menu Bar
        self.proveedores_menubar = wx.MenuBar()
        self.name_editar_proveedor = wx.Menu()
        self.name_eliminar_proveedor = wx.MenuItem(self.name_editar_proveedor, 201, ("Eliminar..."), ("Eliminar proveedor"), wx.ITEM_NORMAL)
        self.name_editar_proveedor.AppendItem(self.name_eliminar_proveedor)
        self.name_modificar_proveedor = wx.MenuItem(self.name_editar_proveedor, 202, ("Modificar..."), (u"Modificar informaci\u00f3n de un proveedor"), wx.ITEM_NORMAL)
        self.name_editar_proveedor.AppendItem(self.name_modificar_proveedor)
        self.name_nuevo_proveedor = wx.MenuItem(self.name_editar_proveedor, 203, ("Nuevo..."), (u"A\u00f1adir un nuevo proveedor"), wx.ITEM_NORMAL)
        self.name_editar_proveedor.AppendItem(self.name_nuevo_proveedor)
        self.proveedores_menubar.Append(self.name_editar_proveedor, ("Editar..."))
        self.SetMenuBar(self.proveedores_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.proveedores_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.proveedores_toolbar)
        self.proveedores_toolbar.AddLabelTool(204, ("Primero"), wx.Bitmap("/home/td/BMPS/FRSREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Primer proveedor"), ("Mostrar datos del primer proveedor"))
        self.proveedores_toolbar.AddLabelTool(205, ("Anterior"), wx.Bitmap("/home/td/BMPS/PRVREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Anterior proveedor"), ("Mostrar datos del anterior proveedor"))
        self.proveedores_toolbar.AddLabelTool(206, ("Siguiente"), wx.Bitmap("/home/td/BMPS/NXTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Siguiente proveedor"), ("Mostrar datos del siguiente proveedor"))
        self.proveedores_toolbar.AddLabelTool(207, (u"\u00daltimo"), wx.Bitmap("/home/td/BMPS/LSTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"\u00daltimo proveedor"), (u"Mostrar datos del \u00faltimo proveedor"))
        self.proveedores_toolbar.AddLabelTool(208, ("Salir"), wx.Bitmap("/home/td/BMPS/CLOSE.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Salir de esta ventana"), (u"Volver al men\u00fa principal"))
        # Tool Bar end
        self.label_titulo_proveedor = wx.StaticText(self, wx.ID_ANY, ("PROVEEDORES"))
        self.label_cif_proveedor = wx.StaticText(self, wx.ID_ANY, ("CIF"))
        self.text_ctrl_cif_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_razon_proveedor = wx.StaticText(self, wx.ID_ANY, (u"Raz\u00f3n"))
        self.text_ctrl_razon_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_alias_proveedor = wx.StaticText(self, wx.ID_ANY, ("Alias"))
        self.text_ctrl_alias_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_actividad_proveedor = wx.StaticText(self, wx.ID_ANY, ("Actividad"))
        self.text_ctrl_actividad_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_calle_proveedor = wx.StaticText(self, wx.ID_ANY, ("Calle"))
        self.text_ctrl_calle_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_portal_proveedor = wx.StaticText(self, wx.ID_ANY, ("Portal"))
        self.text_ctrl_portal_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_piso_proveedor = wx.StaticText(self, wx.ID_ANY, ("Piso"))
        self.text_ctrl_piso_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_localidad_proveedor = wx.StaticText(self, wx.ID_ANY, ("Localidad"))
        self.text_ctrl_localidad_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_cp_proveedor = wx.StaticText(self, wx.ID_ANY, (u"C\u00f3digo postal"))
        self.text_ctrl_cp_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_provincia_proveedor = wx.StaticText(self, wx.ID_ANY, ("Provincia"))
        self.text_ctrl_provincia_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_pais_proveedor = wx.StaticText(self, wx.ID_ANY, (u"Pa\u00eds"))
        self.text_ctrl_pais_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_1_proveedor = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono 1"))
        self.text_ctrl_tel_1_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_tel_2_proveedor = wx.StaticText(self, wx.ID_ANY, (u"Tel\u00e9fono 2"))
        self.text_ctrl_tel_2_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_fax_proveedor = wx.StaticText(self, wx.ID_ANY, ("Fax"))
        self.text_ctrl_fax_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_pag_web_proveedor = wx.StaticText(self, wx.ID_ANY, (u"P\u00e1gina web"))
        self.text_ctrl_pag_web_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_email_proveedor = wx.StaticText(self, wx.ID_ANY, (u"Correo electr\u00f3nico"))
        self.text_ctrl_email_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_num_cuenta_proveedor = wx.StaticText(self, wx.ID_ANY, (u"N\u00famero de cuenta"))
        self.text_ctrl_num_cuenta_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_persona_contacto_1_proveedor = wx.StaticText(self, wx.ID_ANY, ("Persona de contacto 1"))
        self.text_ctrl_persona_contacto_1_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_persona_contacto_2_proveedor = wx.StaticText(self, wx.ID_ANY, ("Persona de contacto 2"))
        self.text_ctrl_persona_contacto_2_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_empty_proveedor = wx.StaticText(self, wx.ID_ANY, ("ID"))
        self.text_ctrl_empty_proveedor = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_aceptar_proveedor = wx.Button(self, wx.ID_ANY, ("ACEPTAR"))

        self.rellenarDatos()
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.eliminar_proveedor, self.name_eliminar_proveedor)
        self.Bind(wx.EVT_MENU, self.modificar_proveedor, self.name_modificar_proveedor)
        self.Bind(wx.EVT_MENU, self.nuevo_proveedor, self.name_nuevo_proveedor)
        self.Bind(wx.EVT_TOOL, self.primer_proveedor, id=204)
        self.Bind(wx.EVT_TOOL, self.anterior_proveedor, id=205)
        self.Bind(wx.EVT_TOOL, self.siguiente_proveedor, id=206)
        self.Bind(wx.EVT_TOOL, self.ultimo_proveedor, id=207)
        self.Bind(wx.EVT_TOOL, self.salir_proveedor, id=208)
        self.Bind(wx.EVT_BUTTON, self.on_button_aceptar_proveedor, self.button_aceptar_proveedor)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Proveedores.__set_properties
        self.SetTitle((u"Proveedores - Almac\u00e9n"))
        self.proveedores_toolbar.Realize()
        self.label_empty_proveedor.Hide()
        self.text_ctrl_empty_proveedor.Hide()
        self.button_aceptar_proveedor.Disable()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Proveedores.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(10, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(10, 2, 0, 0)
        sizer_3.Add(self.label_titulo_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_cif_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_cif_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_razon_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_razon_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_alias_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_alias_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_actividad_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_actividad_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_calle_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_calle_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_portal_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_portal_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_piso_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_piso_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_localidad_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_localidad_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_cp_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_cp_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.label_provincia_proveedor, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_provincia_proveedor, 0, 0, 0)
        sizer_4.Add(grid_sizer_1, 1, 0, 0)
        grid_sizer_2.Add(self.label_pais_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_pais_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_1_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_1_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_tel_2_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_tel_2_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_fax_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_fax_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_pag_web_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_pag_web_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_email_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_email_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_num_cuenta_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_num_cuenta_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_persona_contacto_1_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_persona_contacto_1_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_persona_contacto_2_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_persona_contacto_2_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.label_empty_proveedor, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_empty_proveedor, 0, 0, 0)
        sizer_4.Add(grid_sizer_2, 1, 0, 0)
        sizer_3.Add(sizer_4, 1, 0, 0)
        sizer_3.Add(self.button_aceptar_proveedor, 0, 0, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def rellenarDatos(self):
        self.text_ctrl_cif_proveedor.AppendText(str(self.lista[self.pos].cif))
        self.text_ctrl_razon_proveedor.AppendText(str(self.lista[self.pos].razon))
        self.text_ctrl_alias_proveedor.AppendText(str(self.lista[self.pos].alias))
        self.text_ctrl_actividad_proveedor.AppendText(str(self.lista[self.pos].actividad))
        self.text_ctrl_calle_proveedor.AppendText(str(self.lista[self.pos].calle))
        self.text_ctrl_portal_proveedor.AppendText(str(self.lista[self.pos].portal))
        self.text_ctrl_piso_proveedor.AppendText(str(self.lista[self.pos].piso))
        self.text_ctrl_localidad_proveedor.AppendText(str(self.lista[self.pos].localidad))
        self.text_ctrl_cp_proveedor.AppendText(str(self.lista[self.pos].cp))
        self.text_ctrl_provincia_proveedor.AppendText(str(self.lista[self.pos].provincia))
        self.text_ctrl_pais_proveedor.AppendText(str(self.lista[self.pos].pais))
        self.text_ctrl_tel_1_proveedor.AppendText(str(self.lista[self.pos].tel1))
        self.text_ctrl_tel_2_proveedor.AppendText(str(self.lista[self.pos].tel2))
        self.text_ctrl_fax_proveedor.AppendText(str(self.lista[self.pos].fax))
        self.text_ctrl_pag_web_proveedor.AppendText(str(self.lista[self.pos].pag_web))
        self.text_ctrl_email_proveedor.AppendText(str(self.lista[self.pos].email))
        self.text_ctrl_num_cuenta_proveedor.AppendText(str(self.lista[self.pos].n_cuenta))
        self.text_ctrl_persona_contacto_1_proveedor.AppendText(str(self.lista[self.pos].persona_contacto1))
        self.text_ctrl_persona_contacto_2_proveedor.AppendText(str(self.lista[self.pos].persona_contacto2))
        self.text_ctrl_empty_proveedor.AppendText(str(self.lista[self.pos].identificador))

    def limpiarDatos(self):
        self.text_ctrl_cif_proveedor.SetValue("")
        self.text_ctrl_razon_proveedor.SetValue("")
        self.text_ctrl_alias_proveedor.SetValue("")
        self.text_ctrl_actividad_proveedor.SetValue("")
        self.text_ctrl_calle_proveedor.SetValue("")
        self.text_ctrl_portal_proveedor.SetValue("")
        self.text_ctrl_piso_proveedor.SetValue("")
        self.text_ctrl_localidad_proveedor.SetValue("")
        self.text_ctrl_cp_proveedor.SetValue("")
        self.text_ctrl_provincia_proveedor.SetValue("")
        self.text_ctrl_pais_proveedor.SetValue("")
        self.text_ctrl_tel_1_proveedor.SetValue("")
        self.text_ctrl_tel_2_proveedor.SetValue("")
        self.text_ctrl_fax_proveedor.SetValue("")
        self.text_ctrl_pag_web_proveedor.SetValue("")
        self.text_ctrl_email_proveedor.SetValue("")
        self.text_ctrl_num_cuenta_proveedor.SetValue("")
        self.text_ctrl_persona_contacto_1_proveedor.SetValue("")
        self.text_ctrl_persona_contacto_2_proveedor.SetValue("")
        self.text_ctrl_empty_proveedor.SetValue("")


    def crearProveedorInsertar(self):
        self.proveedorVariacion.identificador = self.ultimo
        self.proveedorVariacion.cif = self.text_ctrl_cif_proveedor.GetValue()
        self.proveedorVariacion.razon = self.text_ctrl_razon_proveedor.GetValue()
        self.proveedorVariacion.alias = self.text_ctrl_alias_proveedor.GetValue()
        self.proveedorVariacion.actividad = self.text_ctrl_actividad_proveedor.GetValue()
        self.proveedorVariacion.calle = self.text_ctrl_calle_proveedor.GetValue()
        self.proveedorVariacion.portal = self.text_ctrl_portal_proveedor.GetValue()
        self.proveedorVariacion.piso = self.text_ctrl_piso_proveedor.GetValue()
        self.proveedorVariacion.localidad = self.text_ctrl_localidad_proveedor.GetValue()
        self.proveedorVariacion.cp = self.text_ctrl_cp_proveedor.GetValue()
        self.proveedorVariacion.provincia = self.text_ctrl_provincia_proveedor.GetValue()
        self.proveedorVariacion.pais = self.text_ctrl_pais_proveedor.GetValue()
        self.proveedorVariacion.tel1 = self.text_ctrl_tel_1_proveedor.GetValue()
        self.proveedorVariacion.tel2 = self.text_ctrl_tel_2_proveedor.GetValue()
        self.proveedorVariacion.fax = self.text_ctrl_fax_proveedor.GetValue()
        self.proveedorVariacion.pag_web = self.text_ctrl_pag_web_proveedor.GetValue()
        self.proveedorVariacion.email = self.text_ctrl_email_proveedor.GetValue()
        self.proveedorVariacion.n_cuenta = self.text_ctrl_num_cuenta_proveedor.GetValue()
        self.proveedorVariacion.persona_contacto1 = self.text_ctrl_persona_contacto_1_proveedor.GetValue()
        self.proveedorVariacion.persona_contacto2 = self.text_ctrl_persona_contacto_2_proveedor.GetValue()


    def crearProveedor(self):
        self.proveedorVariacion.identificador = self.text_ctrl_empty_proveedor.GetValue()
        self.proveedorVariacion.cif = self.text_ctrl_cif_proveedor.GetValue()
        self.proveedorVariacion.razon = self.text_ctrl_razon_proveedor.GetValue()
        self.proveedorVariacion.alias = self.text_ctrl_alias_proveedor.GetValue()
        self.proveedorVariacion.actividad = self.text_ctrl_actividad_proveedor.GetValue()
        self.proveedorVariacion.calle = self.text_ctrl_calle_proveedor.GetValue()
        self.proveedorVariacion.portal = self.text_ctrl_portal_proveedor.GetValue()
        self.proveedorVariacion.piso = self.text_ctrl_piso_proveedor.GetValue()
        self.proveedorVariacion.localidad = self.text_ctrl_localidad_proveedor.GetValue()
        self.proveedorVariacion.cp = self.text_ctrl_cp_proveedor.GetValue()
        self.proveedorVariacion.provincia = self.text_ctrl_provincia_proveedor.GetValue()
        self.proveedorVariacion.pais = self.text_ctrl_pais_proveedor.GetValue()
        self.proveedorVariacion.tel1 = self.text_ctrl_tel_1_proveedor.GetValue()
        self.proveedorVariacion.tel2 = self.text_ctrl_tel_2_proveedor.GetValue()
        self.proveedorVariacion.fax = self.text_ctrl_fax_proveedor.GetValue()
        self.proveedorVariacion.pag_web = self.text_ctrl_pag_web_proveedor.GetValue()
        self.proveedorVariacion.email = self.text_ctrl_email_proveedor.GetValue()
        self.proveedorVariacion.n_cuenta = self.text_ctrl_num_cuenta_proveedor.GetValue()
        self.proveedorVariacion.persona_contacto1 = self.text_ctrl_persona_contacto_1_proveedor.GetValue()
        self.proveedorVariacion.persona_contacto2 = self.text_ctrl_persona_contacto_2_proveedor.GetValue()

    
    def cambiarPrimerProveedor(self):
        self.pos = 0
        self.limpiarDatos()
        self.rellenarDatos()

    def cambiarAnteriorProveedor(self):
        if (self.pos > 0):
            self.pos = self.pos - 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarProveedor(self):
        if (self.pos < len(self.lista)-1):
            self.pos = self.pos + 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarUltimoProveedor(self):
        self.pos = len(self.lista)-1
        self.limpiarDatos()
        self.rellenarDatos()


    def eliminar_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.crearProveedor()
        self.con.eliminarProveedor(self.proveedorVariacion)
        self.lista = self.con.consultarProveedor()
        self.limpiarDatos()
        self.pos=0
        self.rellenarDatos()
        print "Eliminando registro..."
        event.Skip()

    def modificar_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.button_aceptar_proveedor.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.operacion = 2
        print "Modificando registro..."
        event.Skip()

    def nuevo_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.button_aceptar_proveedor.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.limpiarDatos()
        self.operacion=1
        print "Anhadiendo registro..."
        event.Skip()

    def primer_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.cambiarPrimerProveedor()
        event.Skip()

    def anterior_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.cambiarAnteriorProveedor()
        event.Skip()

    def siguiente_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.cambiarProveedor()
        event.Skip()

    def ultimo_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        self.cambiarUltimoProveedor()
        event.Skip()

    def salir_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        print "Volviendo a la página principal..."
        commands.getoutput('./. interfaz.py')
        self.ventana=Principal(None, wx.ID_ANY, "")
        self.ventana.Show()
        self.Close()
        event.Skip()

    def on_button_aceptar_proveedor(self, event):  # wxGlade: Proveedores.<event_handler>
        #DESHABILITAR BOTÓN DESPUÉS DE HACER LA OPERACIÓN
        if (self.operacion == 1):
            self.crearProveedorInsertar()
            self.con.insertarProveedor(self.proveedorVariacion,self.ultimo)
            self.lista = self.con.consultarProveedor()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        elif (self.operacion == 2):
            self.crearProveedor()
            self.con.modificarProveedor(self.proveedorVariacion)
            self.lista = self.con.consultarProveedor()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        print "Aplicando cambios..."
        self.button_aceptar_proveedor.Disable()
        event.Skip()

# end of class Proveedores

class Articulos(wx.Frame):
    def __init__(self, *args, **kwds):
        self.operacion = 0
        self.con=connection()
        self.lista = self.con.consultarArticulo()
        self.pos = 0
        self.idArticulo = self.lista[self.pos].identificador
        self.articuloVariacion = self.lista[0]
        self.ultimo = len(self.lista)+1
        # begin wxGlade: Articulos.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.Center()
        # Menu Bar
        self.frame_4_menubar = wx.MenuBar()
        self.name_editar_articulo = wx.Menu()
        self.name_eliminar_articulo = wx.MenuItem(self.name_editar_articulo, 301, ("Eliminar..."), ("Eliminar articulo"), wx.ITEM_NORMAL)
        self.name_editar_articulo.AppendItem(self.name_eliminar_articulo)
        self.name_modificar_articulo = wx.MenuItem(self.name_editar_articulo, 302, ("Modificar..."), (u"Modificar informaci\u00f3n de un art\u00edculo"), wx.ITEM_NORMAL)
        self.name_editar_articulo.AppendItem(self.name_modificar_articulo)
        self.name_nuevo_articulo = wx.MenuItem(self.name_editar_articulo, 303, ("Nuevo..."), (u"A\u00f1adir nuevo art\u00edculo"), wx.ITEM_NORMAL)
        self.name_editar_articulo.AppendItem(self.name_nuevo_articulo)
        self.frame_4_menubar.Append(self.name_editar_articulo, ("Editar..."))
        self.SetMenuBar(self.frame_4_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.frame_4_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_4_toolbar)
        self.frame_4_toolbar.AddLabelTool(304, ("Primero"), wx.Bitmap("/home/td/BMPS/FRSREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"Primer art\u00edculo"), (u"Mostrar datos del primer art\u00edculo"))
        self.frame_4_toolbar.AddLabelTool(305, ("Anterior"), wx.Bitmap("/home/td/BMPS/PRVREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"Anterior art\u00edculo"), (u"Mostrar datos del anterior art\u00edculo"))
        self.frame_4_toolbar.AddLabelTool(306, ("Siguiente"), wx.Bitmap("/home/td/BMPS/NXTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"Siguiente art\u00edculo"), (u"Mostrar datos del siguiente art\u00edculo"))
        self.frame_4_toolbar.AddLabelTool(307, (u"\u00daltimo"), wx.Bitmap("/home/td/BMPS/LSTREC_S.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, (u"\u00daltimo art\u00edculo"), (u"Mostrar datos del \u00faltimo art\u00edculo"))
        self.frame_4_toolbar.AddLabelTool(308, ("Salir"), wx.Bitmap("/home/td/BMPS/CLOSE.BMP", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, ("Salir de esta ventana"), (u"Volver al men\u00fa principal"))
        # Tool Bar end
        self.label_titulo_articulo = wx.StaticText(self, wx.ID_ANY, (u"ART\u00cdCULOS"))
        self.label_codigo_articulo = wx.StaticText(self, wx.ID_ANY, (u"C\u00f3digo"))
        self.text_ctrl_codigo_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_descrip_articulo = wx.StaticText(self, wx.ID_ANY, (u"Descripci\u00f3n"))
        self.text_ctrl_descrip_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_pvp_articulo = wx.StaticText(self, wx.ID_ANY, ("PVP"))
        self.text_ctrl_pvp_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_unidades_articulo = wx.StaticText(self, wx.ID_ANY, ("Unidades"))
        self.text_ctrl_unidades_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_stock_seg_articulo = wx.StaticText(self, wx.ID_ANY, ("Stock de seguridad"))
        self.text_ctrl_stock_seg_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_stock_mini_articulo = wx.StaticText(self, wx.ID_ANY, (u"Stock m\u00ednimo"))
        self.text_ctrl_stock_mini_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_pm_coste_articulo = wx.StaticText(self, wx.ID_ANY, (u"Valoraci\u00f3n precio medio"))
        self.text_ctrl_pm_coste_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_ult_pcoste_articulo = wx.StaticText(self, wx.ID_ANY, (u"\u00daltimo precio coste"))
        self.text_ctrl_ult_pcoste_articulo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_aceptar_articulo = wx.Button(self, wx.ID_ANY, ("ACEPTAR"))

        self.rellenarDatos()
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.eliminar_articulo, self.name_eliminar_articulo)
        self.Bind(wx.EVT_MENU, self.modificar_articulo, self.name_modificar_articulo)
        self.Bind(wx.EVT_MENU, self.nuevo_articulo, self.name_nuevo_articulo)
        self.Bind(wx.EVT_TOOL, self.primer_articulo, id=304)
        self.Bind(wx.EVT_TOOL, self.anterior_articulo, id=305)
        self.Bind(wx.EVT_TOOL, self.siguiente_articulo, id=306)
        self.Bind(wx.EVT_TOOL, self.ultimo_articulo, id=307)
        self.Bind(wx.EVT_TOOL, self.salir_articulo, id=308)
        self.Bind(wx.EVT_BUTTON, self.on_button_aceptar_articulo, self.button_aceptar_articulo)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Articulos.__set_properties
        self.SetTitle((u"Art\u00edculos - Almac\u00e9n"))
        self.frame_4_toolbar.Realize()
        self.button_aceptar_articulo.Disable()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Articulos.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_4 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_3 = wx.GridSizer(4, 2, 0, 0)
        sizer_3.Add(self.label_titulo_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.label_codigo_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.text_ctrl_codigo_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.label_descrip_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.text_ctrl_descrip_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.label_pvp_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.text_ctrl_pvp_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.label_unidades_articulo, 0, 0, 0)
        grid_sizer_3.Add(self.text_ctrl_unidades_articulo, 0, 0, 0)
        sizer_4.Add(grid_sizer_3, 1, 0, 0)
        grid_sizer_4.Add(self.label_stock_seg_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.text_ctrl_stock_seg_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.label_stock_mini_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.text_ctrl_stock_mini_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.label_pm_coste_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.text_ctrl_pm_coste_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.label_ult_pcoste_articulo, 0, 0, 0)
        grid_sizer_4.Add(self.text_ctrl_ult_pcoste_articulo, 0, 0, 0)
        sizer_4.Add(grid_sizer_4, 1, 0, 0)
        sizer_3.Add(sizer_4, 1, 0, 0)
        sizer_3.Add(self.button_aceptar_articulo, 0, 0, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade


    def rellenarDatos(self):
        self.text_ctrl_codigo_articulo.AppendText(str(self.lista[self.pos].codigo))
        self.text_ctrl_descrip_articulo.AppendText(str(self.lista[self.pos].descrip))
        self.text_ctrl_pvp_articulo.AppendText(str(self.lista[self.pos].pvp))
        self.text_ctrl_unidades_articulo.AppendText(str(self.lista[self.pos].unidades))
        self.text_ctrl_stock_seg_articulo.AppendText(str(self.lista[self.pos].stock_seg))
        self.text_ctrl_stock_mini_articulo.AppendText(str(self.lista[self.pos].stock_min))
        self.text_ctrl_pm_coste_articulo.AppendText(str(self.lista[self.pos].pm_coste))
        self.text_ctrl_ult_pcoste_articulo.AppendText(str(self.lista[self.pos].ult_pcoste))
        self.idArticulo = str(self.lista[self.pos].identificador)


    def limpiarDatos(self):
        self.text_ctrl_codigo_articulo.SetValue("")
        self.text_ctrl_descrip_articulo.SetValue("")
        self.text_ctrl_pvp_articulo.SetValue("")
        self.text_ctrl_unidades_articulo.SetValue("")
        self.text_ctrl_stock_seg_articulo.SetValue("")
        self.text_ctrl_stock_mini_articulo.SetValue("")
        self.text_ctrl_pm_coste_articulo.SetValue("")
        self.text_ctrl_ult_pcoste_articulo.SetValue("")
        self.idArticulo = "0"


    def crearArticuloInsertar(self):
        self.articuloVariacion.identificador = self.ultimo
        self.articuloVariacion.codigo = self.text_ctrl_codigo_articulo.GetValue()
        self.articuloVariacion.descrip = self.text_ctrl_descrip_articulo.GetValue()
        self.articuloVariacion.pvp = self.text_ctrl_pvp_articulo.GetValue()
        self.articuloVariacion.unidades = self.text_ctrl_unidades_articulo.GetValue()
        self.articuloVariacion.stock_seg = self.text_ctrl_stock_seg_articulo.GetValue()
        self.articuloVariacion.stock_min = self.text_ctrl_stock_mini_articulo.GetValue()
        self.articuloVariacion.pm_coste = self.text_ctrl_pm_coste_articulo.GetValue()
        self.articuloVariacion.ult_pcoste = self.text_ctrl_ult_pcoste_articulo.GetValue()

    def crearArticulo(self):
        self.articuloVariacion.identificador = self.idArticulo
        self.articuloVariacion.codigo = self.text_ctrl_codigo_articulo.GetValue()
        self.articuloVariacion.descrip = self.text_ctrl_descrip_articulo.GetValue()
        self.articuloVariacion.pvp = self.text_ctrl_pvp_articulo.GetValue()
        self.articuloVariacion.unidades = self.text_ctrl_unidades_articulo.GetValue()
        self.articuloVariacion.stock_seg = self.text_ctrl_stock_seg_articulo.GetValue()
        self.articuloVariacion.stock_min = self.text_ctrl_stock_mini_articulo.GetValue()
        self.articuloVariacion.pm_coste = self.text_ctrl_pm_coste_articulo.GetValue()
        self.articuloVariacion.ult_pcoste = self.text_ctrl_ult_pcoste_articulo.GetValue()


    def cambiarPrimerArticulo(self):
            self.pos = 0
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarAnteriorArticulo(self):
        if (self.pos > 0):
            self.pos = self.pos - 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarArticulo(self):
        if (self.pos < len(self.lista)-1):
            self.pos = self.pos + 1
            self.limpiarDatos()
            self.rellenarDatos()

    def cambiarUltimoArticulo(self):
            self.pos = len(self.lista)-1
            self.limpiarDatos()
            self.rellenarDatos()


    def eliminar_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.crearArticulo()
        self.con.eliminarArticulo(self.articuloVariacion)
        self.lista = self.con.consultarArticulo()
        self.limpiarDatos()
        self.pos=0
        self.rellenarDatos()
        print "Eliminando registro..."
        event.Skip()


    def modificar_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.button_aceptar_articulo.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.operacion = 2
        print "Modificando registro..."
        event.Skip()


    def nuevo_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.button_aceptar_articulo.Enable()
        #HABILITAR BOTÓN ACEPTAR Y UNA VARIABLE QUE DICE SI ES UPDATE, INSERT
        self.limpiarDatos()
        self.operacion=1
        print "Anhadiendo registro..."
        event.Skip()

    def primer_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.cambiarPrimerArticulo()
        event.Skip()

    def anterior_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.cambiarAnteriorArticulo()
        event.Skip()

    def siguiente_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.cambiarArticulo()
        event.Skip()

    def ultimo_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        self.cambiarUltimoArticulo()
        event.Skip()

    def salir_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        print "Volviendo a la página principal..."
        commands.getoutput('./. interfaz.py')
        self.ventana=Principal(None, wx.ID_ANY, "")
        self.ventana.Show()
        self.Close()
        event.Skip()

    def on_button_aceptar_articulo(self, event):  # wxGlade: Articulos.<event_handler>
        if (self.operacion == 1):
            self.crearArticuloInsertar()
            self.con.insertarArticulo(self.articuloVariacion,self.ultimo)
            self.lista = self.con.consultarArticulo()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        elif (self.operacion == 2):
            self.crearArticulo()
            self.con.modificarArticulo(self.articuloVariacion)
            self.lista = self.con.consultarArticulo()
            self.limpiarDatos()
            self.pos=0
            self.rellenarDatos()
        print "Aplicando cambios..."
        self.button_aceptar_articulo.Disable()
        event.Skip()

# end of class Articulos

