from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsVectorDataProvider,
                       QgsFeatureIterator,
                       QgsFeature,
                       QgsCoordinateTransformContext,
                       QgsVectorFileWriter)

path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

layer_memory = QgsVectorLayer("Polygon",
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
    f.setGeometry(feature.geometry())

    layer_memory_dp.addFeature(f)


layer_memory.updateExtents()

print(layer_memory.extent())

print(layer_memory.featureCount())
print(layer_memory.crs())

file_writer_options = QgsVectorFileWriter.SaveVectorOptions()
file_writer_options.fileEncoding = "UTF-8"
file_writer_options.driverName = "GeoJSON"

QgsVectorFileWriter.writeAsVectorFormatV2(layer_memory,
                                          str(path_data.parent / "data_from_memory.geojson"),
                                          QgsCoordinateTransformContext(),
                                          options=file_writer_options)
