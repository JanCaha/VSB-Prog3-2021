from qgis.PyQt.QtCore import QCoreApplication

from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingFeatureSource,
                       QgsWkbTypes,
                       QgsFeature,
                       QgsGeometry,
                       QgsRectangle)

from qgis import processing


class PolygonToBBAlgorithm(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return PolygonToBBAlgorithm()

    def name(self):
        return 'polygon2bb'

    def displayName(self):
        return self.tr('Polygon to bounding box')

    def group(self):
        return self.tr('Example scripts')

    def groupId(self):
        return 'examplescripts'

    def shortHelpString(self):
        return self.tr("Converts polygons to their bounding boxes.")

    def initAlgorithm(self, config=None):

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):

        source: QgsProcessingFeatureSource = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )

        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        input_fields = source.fields()

        sink: QgsFeatureSink
        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            input_fields,
            QgsWkbTypes.Polygon,
            source.sourceCrs()
        )

        feedback.pushInfo('CRS is {}'.format(source.sourceCrs().authid()))

        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        total = 100.0 / source.featureCount() if source.featureCount() else 0

        features = source.getFeatures()

        feature: QgsFeature

        for current_index, feature in enumerate(features):

            if feedback.isCanceled():
                break

            geom: QgsGeometry = feature.geometry()
            attributes = feature.attributes()

            rect: QgsRectangle = geom.boundingBox()

            new_geom = QgsGeometry().fromWkt(rect.asWktPolygon())

            new_feature = QgsFeature(input_fields)
            new_feature.setGeometry(new_geom)
            new_feature.setAttributes(attributes)

            sink.addFeature(new_feature)

            feedback.setProgress(int(current_index * total))

        return {self.OUTPUT: dest_id}
