from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsCoordinateReferenceSystem)

path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

print(input_layer)
print(input_layer.name())
print(input_layer.crs())
print(input_layer.geometryType())
print(input_layer.dataUrl())
print(input_layer.extent())
print(F"Feature count for layer {input_layer.featureCount()}.")

input_layer_crs: QgsCoordinateReferenceSystem = input_layer.crs()

print(input_layer_crs.authid())
print(input_layer_crs.toWkt())
