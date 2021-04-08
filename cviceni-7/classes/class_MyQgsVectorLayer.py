from pathlib import Path

from qgis.core import (QgsVectorLayer,
                       QgsVectorDataProvider,
                       QgsFeature,
                       QgsGeometry)


class MyQgsVectorLayer(QgsVectorLayer):

    def __init__(self, data_path: Path):
        super().__init__(str(data_path))

    def get_data_provider(self) -> QgsVectorDataProvider:
        return self.dataProvider()

    def __repr__(self):
        return "QgsVectorLayer `{}` with {} elements.".format(self.get_data_provider().dataSourceUri(),
                                                              self.get_data_provider().featureCount())

    def features_fid_2(self, external_geom: QgsGeometry = None) -> list[QgsFeature]:

        features = []

        feature: QgsFeature

        for number, feature in enumerate(self.getFeatures()):

            if feature.id() % 2 == 0:
                features.append(feature)

        return features
