from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsCoordinateReferenceSystem,
                       QgsFields,
                       QgsField,
                       QgsFeature,
                       QgsGeometry,
                       QgsVectorFileWriter,
                       QgsWkbTypes,
                       QgsCoordinateTransformContext,
                       QgsRectangle)

path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

path_data_output = path_data.parent / "result.gpkg"

input_layer = QgsVectorLayer(str(path_data))

input_fields: QgsFields = input_layer.fields()

file_writer_options = QgsVectorFileWriter.SaveVectorOptions()
file_writer_options.fileEncoding = "UTF-8"

file_writer: QgsVectorFileWriter = QgsVectorFileWriter.create(str(path_data_output),
                                                              input_fields,
                                                              QgsWkbTypes.Polygon,
                                                              input_layer.crs(),
                                                              QgsCoordinateTransformContext(),
                                                              file_writer_options)

input_features = input_layer.getFeatures()

feature: QgsFeature

for feature in input_features:

    geom: QgsGeometry = feature.geometry()
    attributes = feature.attributes()

    rect: QgsRectangle = geom.boundingBox()

    new_geom = QgsGeometry().fromWkt(rect.asWktPolygon())

    new_feature = QgsFeature(input_fields)
    new_feature.setGeometry(new_geom)
    new_feature.setAttributes(attributes)

    file_writer.addFeature(new_feature)

del file_writer
