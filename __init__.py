# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gazetteerSearch
                                 A QGIS plugin
 Gazetteer
Search plugin
                             -------------------
        begin                : 2012-07-21
        copyright            : (C) 2012 by Rudi von Staden, Nathan Woodrow
        email                : rudivs@gmail.com
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
    return "Gazetteer"
def description():
    return "Gazetteer Search plugin"
def version():
    return "Version 0.3.1"
def icon():
    return "icon.svg"
def qgisMinimumVersion():
    return "1.8"
def author():
    return "Rudi von Staden"
def email():
    return "rudivs@gmail.com"

def classFactory(iface):
    # Add the directory that this file live in to the start of sys.path
    # so that imports can be relative and our modules have the highest priority
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    # Load gazetteerSearch class from file gazetteerSearch
    from gazetteersearch import gazetteerSearch
    return gazetteerSearch(iface)
