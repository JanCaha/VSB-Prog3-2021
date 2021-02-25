from osgeo import ogr

ds: ogr.DataSource = ogr.Open("cesta/k/souboru", True)

ds.GetLayerCount()

layer: ogr.Layer = ds.GetLayer()

layer.GetName()
