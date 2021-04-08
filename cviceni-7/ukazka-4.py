from pathlib import Path

from classes.class_MyQgsVectorLayer import MyQgsVectorLayer

path_data = Path(__file__).parent.parent / "_data" / "nc.gpkg"

input_layer = MyQgsVectorLayer(path_data)

print(input_layer.extent())
print(input_layer.crs())

print(input_layer)

input_layer_dp = input_layer.get_data_provider()
print(input_layer_dp)

features = input_layer.features_fid_2()

print(len(features))
print(features[0])
