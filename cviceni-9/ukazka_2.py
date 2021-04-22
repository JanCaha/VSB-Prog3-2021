from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsVectorFileWriter,
                       QgsVectorDataProvider,
                       QgsFeatureIterator,
                       QgsFeature,
                       QgsGeometry,
                       QgsPolygon,
                       QgsCoordinateTransformContext)


path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

layer_memory = QgsVectorLayer("Point",
                              "layer_in_memory",
                              "memory")

layer_memory.setCrs(input_layer.crs())

layer_memory_dp: QgsVectorDataProvider = layer_memory.dataProvider()

layer_memory_dp.addAttributes(input_layer.fields())

layer_memory.updateFields()

features: QgsFeatureIterator = input_layer.getFeatures()

feature: QgsFeature

for feature in features:

    f = QgsFeature()
    f.setAttributes(feature.attributes())

    geom: QgsGeometry = feature.geometry()
    length = geom.length()

    polygon = QgsPolygon()
    polygon.fromWkt(geom.asWkt())

    print(geom)
    print(polygon)
    print("*" * 60)

    new_geom: QgsGeometry = geom.interpolate(length/2)

    f.setGeometry(new_geom)

    layer_memory_dp.addFeature(f)


layer_memory.updateExtents()

file_writer_options = QgsVectorFileWriter.SaveVectorOptions()
file_writer_options.fileEncoding = "UTF-8"

QgsVectorFileWriter.writeAsVectorFormatV2(layer_memory,
                                          str(path_data.parent / "points.gpkg"),
                                          QgsCoordinateTransformContext(),
                                          options=file_writer_options)
