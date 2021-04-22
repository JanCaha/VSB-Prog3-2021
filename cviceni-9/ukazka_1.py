from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsCoordinateReferenceSystem,
                       QgsProperty,
                       QgsExpression)

from qgis.core import QgsApplication
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms
from processing.core.parameters import QgsProcessingParameterExpression

app = QgsApplication([], False)
Processing.initialize()
app.processingRegistry().addProvider(QgsNativeAlgorithms())


path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = QgsVectorLayer(str(path_data))

processing.run("native:interpolatepoint",
               {'INPUT': input_layer,
                'DISTANCE': QgsExpression('"PERIMETER"').evaluate(),
                'OUTPUT': str(path_data.parent / "points.gpkg")})




