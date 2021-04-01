from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsCoordinateReferenceSystem)

from qgis.core import QgsApplication
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms

app = QgsApplication([], False)
Processing.initialize()
app.processingRegistry().addProvider(QgsNativeAlgorithms())


path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

layer_name = "layer_with_fixed_geometries"

params = {'INPUT': input_layer,
          'OUTPUT': "memory:{}".format(layer_name)}

result = processing.run("native:fixgeometries",
                        params)

result_layer: QgsVectorLayer = result["OUTPUT"]

print(result_layer.name())
print(result_layer.crs())
print(result_layer.extent())
print(result_layer.featureCount())

result2 = processing.run("native:reprojectlayer",
                         {'INPUT': result_layer,
                          'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:4269'),
                          'OUTPUT': str(path_data.parent / "reprojected.gpkg")})

print(result2)
print(result2["OUTPUT"])

reprojected_layer = QgsVectorLayer(result2["OUTPUT"])

print(reprojected_layer)
print(reprojected_layer.crs())
