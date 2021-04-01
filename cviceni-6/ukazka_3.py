from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsVectorDataProvider,
                       QgsFeatureIterator,
                       QgsFeature,
                       QgsFields,
                       QgsField,
                       QgsCoordinateTransformContext,
                       QgsVectorFileWriter)

from PyQt5.QtCore import QVariant


path_data = Path(__file__).parent.parent / "_data" / "result.gpkg"

input_layer = QgsVectorLayer(str(path_data))

input_layer.startEditing()

dp_input: QgsVectorDataProvider = input_layer.dataProvider()

new_field_name = "moje_nové_pole"

add_fields = QgsFields()
add_fields.append(QgsField(new_field_name, QVariant.String))

dp_input.addAttributes(add_fields)

input_layer.updateFields()

feature: QgsFeature

for number, feature in enumerate(input_layer.getFeatures()):

    input_layer.changeAttributeValue(feature.id(),
                                     feature.fieldNameIndex(new_field_name),
                                     "hodnota atributu: {}".format(number))

input_layer.commitChanges()
# input_layer.rollBack()
