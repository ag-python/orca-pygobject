# Orca                                                                              
#
# Copyright 2010 Consorcio Fernando de los Rios.
# Author: J. Ignacio Alvarez <jialvarez@emergya.es>                                 
#
# This library is free software; you can redistribute it and/or                     
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.                
#
# This library is distributed in the hope that it will be useful,                   
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU                 
# Lesser General Public License for more details.                                   
#
# You should have received a copy of the GNU Lesser General Public                  
# License along with this library; if not, write to the
# Free Software Foundation, Inc., Franklin Street, Fifth Floor,                     
# Boston MA  02110-1301 USA.                                                        

"""Gets the example window and load it."""      

__id__        = "$Id$"
__version__   = "$Revision$"                                                        
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2010 Consorcio Fernando de los Rios."                
__license__   = "LGPL"                                                              

import os
import sys
from orca import orca_platform

OS = None

class GUIController:
    def __init__(self):
        pass

    def showUI(self, mod):
        global OS
        
        if not OS:
            
            uiFile = os.path.join(orca_platform.prefix,
                                  orca_platform.datadirname,
                                  orca_platform.package,
                                  "gui_manager",
                                  "views",
                                  orca_platform.library,
                                  "ui",
                                  "orca-mainwin.ui")

            OS = mod.OrcaMainGUI(uiFile, "mainWindow")
            OS.init()
        
        OS.showGUI()
    
    def hideUI():
        if OS:
            OS.hideGUI()

