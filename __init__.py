# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gazetteerSearch
                                 A QGIS plugin
 Gazetteer
Search plugin
                             -------------------
        begin                : 2012-07-21
        copyright            : (C) 2012 by Nathan Woodrow
        email                : woodrow.nathan@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import sys
import os


def name():
    return "Gazetteer Search plugin"
def description():
    return "Gazetteer Search plugin"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.8"
def classFactory(iface):
    # Add the directory that this file live in to the start of sys.path
    # so that imports can be relative and our modules have the highest priority
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    # Load gazetteerSearch class from file gazetteerSearch
    from gazetteersearch import gazetteerSearch
    return gazetteerSearch(iface)
