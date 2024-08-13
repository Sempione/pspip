# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PutSpacedPointsInPolygons
                                 A QGIS plugin
 Approximates the maximum number of points in polygons for a certain minimum
 distance between the points.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-08-09
        copyright            : (C) 2024 by Christian Lesem
        email                : christian@lesem.eu
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

__author__ = 'Christian Lesem'
__date__ = '2024-08-09'
__copyright__ = '(C) 2024 by Christian Lesem'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PutSpacedPointsInPolygons class from file PutSpacedPointsInPolygons.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pspip import PutSpacedPointsInPolygonsPlugin
    return PutSpacedPointsInPolygonsPlugin()
