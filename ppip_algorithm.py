# -*- coding: utf-8 -*-

"""
/***************************************************************************
 PutPointsInPolygons
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
"""

__author__ = 'Christian Lesem'
__date__ = '2024-08-09'
__copyright__ = '(C) 2024 by Christian Lesem'

# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

from qgis import processing

from qgis.PyQt.QtCore import (QCoreApplication,
                              QVariant)

from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterDistance,
                       QgsField,
                       QgsCoordinateReferenceSystem,
                       QgsReferencedRectangle,
                       QgsFeature,
                       QgsFields,
                       QgsWkbTypes,
                       QgsVectorLayer)

class PutPointsInPolygonsAlgorithm(QgsProcessingAlgorithm):
    """
    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    DISTANCE = 'DISTANCE'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # Add the input vector features source (limited to polygon layers).
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        # Add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

        # Add distance parameter.
        self.addParameter(
            QgsProcessingParameterDistance(
                self.DISTANCE,
                self.tr('Distance between points'),
                500,
                self.INPUT
                )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(parameters, self.INPUT, context)

        # Retrieve the distance parameter
        SPACING = self.parameterAsInt(parameters, self.DISTANCE, context)
        
        # Prepare fields that are to be added to the sink (the output layer).
        sink_fields = QgsFields()
        sink_fields.append(QgsField('fid', QVariant.Int))
        sink_fields.append(QgsField('NUMPOINTS', QVariant.Int))

        # Retrieve the sink.
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                context, sink_fields, QgsWkbTypes.MultiPoint, source.sourceCrs())
        
        # Compute the number of steps to display within the progress bar.
        total = 100.0 / source.featureCount() if source.featureCount() else 0

        # Get source EPSG code.       
        crs_epsg = int(source.sourceCrs().authid().split(":")[1])
        # Create CRS object. (This is going to be needed when creating
        # a QgsReferencedRectangle object for example.)
        crs_obj = QgsCoordinateReferenceSystem(crs_epsg, QgsCoordinateReferenceSystem.EpsgCrsId)

        # Get features from source.
        features = source.getFeatures()

        #### THE CENTRAL PART OF THE ALGORITHM
        # Iterate over each feature of the input polygon layer, performing the following steps:
        # + Create a temporary polygon layer and add only one element (containing the feature's geometry).
        #   (This is going to be needed later, when clipping the points.)
        # + Get the feature's bounding box.
        # + Create a grid of points within the above bounding box (-> output: point layer).
        # + Clip the point layer using the temporary polygon layer.
        # + Count the points within the feature polygon, retrieve the count ("NUMPOINTS") from the resulting layer.
        # + Use the "Collect geometries" tool ("native:collect") to transform the remaining point freatures
        #   from the points layer into a single MultiPoint feature, retrieve the resulting geometry
        # + Write the feature's fid, geometry (the above MultiPoint geometry) and the point count ("NUMPOINTS")
        #   into the feature sink.

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked.
            if feedback.isCanceled():
                break

            f_id = feature.id()

            # Create new layer containing only the current feature (only geometry).
            lyr_with_current_feature_only = QgsVectorLayer(f'Polygon?crs={crs_epsg}', f'{source.sourceName()}_temp1', 'memory')
            feature_obj_1 = QgsFeature()
            feature_obj_1.setGeometry(feature.geometry())
            pr = lyr_with_current_feature_only.dataProvider()
            pr.addFeatures([feature_obj_1])

            # Create (rectangular) point grid within current feature's bounding box.
            f_bb = feature.geometry().boundingBox()
            referenced_bb = QgsReferencedRectangle(f_bb, crs_obj)
            points_lyr = processing.run(
                    "qgis:regularpoints", {
                        'EXTENT': referenced_bb,
                        'SPACING':SPACING,
                        'INSET':0,
                        'RANDOMIZE':False,
                        'IS_SPACING':True,
                        'CRS':QgsCoordinateReferenceSystem(f'EPSG:{crs_epsg}'),
                        'OUTPUT':'TEMPORARY_OUTPUT'
                            })["OUTPUT"]
            
            # Clip the points lyr with the feature layer as the overlay.
            points_clipped_lyr = processing.run(
                    "native:clip", {
                        'INPUT' : points_lyr,
                        'OUTPUT' : 'TEMPORARY_OUTPUT',
                        'OVERLAY' : lyr_with_current_feature_only
                    })["OUTPUT"]
            
            # Count the points within the polygon.
            counter_lyr = processing.run("native:countpointsinpolygon", {
                        'POLYGONS': lyr_with_current_feature_only,
                        'POINTS':points_clipped_lyr,
                        'WEIGHT':'',
                        'CLASSFIELD':'',
                        'FIELD':'NUMPOINTS',
                        'OUTPUT':'TEMPORARY_OUTPUT'})["OUTPUT"]

            # Retrieve the number of points from the only feature in the counter layer.            
            numpoints = int(counter_lyr.getFeature(1)["NUMPOINTS"])

            # Make MultiPoint from the single points.
            multipart_points_lyr = processing.run(
                "native:collect", {
                    'INPUT':points_clipped_lyr,
                    'FIELD':[],
                    'OUTPUT':'TEMPORARY_OUTPUT'
                    })["OUTPUT"]
            
            # Create and fill the feature that is to be added to the sink.
            feature_obj_2 = QgsFeature()        
            geom = multipart_points_lyr.getFeature(1).geometry()
            feature_obj_2.setGeometry(geom)
            feature_obj_2.setAttributes([f_id, numpoints])
        
            # Add the feature in the sink.
            sink.addFeature(feature_obj_2, QgsFeatureSink.FastInsert)

            # Update the progress bar.
            feedback.setProgress(int(current * total))

        # TODO: create alternating grids, shift grid and rotate grid gradually
        # to ensure the grid fills the polygon even when shifted or rotated,
        # its size has to exceed the bounding box by at least one time the SPACING 
        # value and it should be a circle

        # Return the results of the algorithm. 
        return {self.OUTPUT: dest_id}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Put points in polygons'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())
    
    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Vector analysis'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return PutPointsInPolygonsAlgorithm()
