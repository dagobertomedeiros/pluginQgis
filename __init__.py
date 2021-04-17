# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SetLocation
                                 A QGIS plugin
 define uma localização
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-04-16
        copyright            : (C) 2021 by Dagoberto Medeiros
        email                : dagobertomedeiros@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SetLocation class from file SetLocation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .set_location import SetLocation
    return SetLocation(iface)
