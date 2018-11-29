# encoding: utf-8
# Propietario: David Tojo

import sys
sys.path.append('./interfaz')
from interfaz import *

class MiApp(wx.App):
    def OnInit(self):
        self.ventana=Principal(None, wx.ID_ANY, "")
        self.SetTopWindow(self.ventana)
        self.ventana.Show()
        return True

aplicacion=MiApp(0)
aplicacion.MainLoop()






