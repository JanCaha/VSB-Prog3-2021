from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsCoordinateReferenceSystem,
                       QgsFields,
                       QgsField,
                       QgsFeature,
                       QgsGeometry)

path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

input_fields: QgsFields = input_layer.fields()


field: QgsField

for field in input_fields:
    print(f"`{field.name()}` of type `{field.typeName()}`")

print("*" * 60)

input_features = input_layer.getFeatures()

feature: QgsFeature

for feature in input_features:

    print(feature.id())

    geom: QgsGeometry = feature.geometry()

    print(geom.asWkt())

    attribute = feature.attribute("NAME")

    print(attribute)
