import os,sys 
import qgis 
import qgis.core

qgis_prefix = os.getenv("QGIS_PREFIX_PATH")      
qgis.core.QgsApplication.setPrefixPath(qgis_prefix, True) 
qgs = qgis.core.QgsApplication([], False)
qgs.initQgis()

# Be sure to change the path to point to where your plugins folder is located
# it may not be the same as this one.
sys.path.append(r"C:\OSGeo4W\apps\qgis-ltr\python\plugins")
import processing 
from processing.core.Processing import Processing 
Processing.initialize() 
qgis.core.QgsApplication.processingRegistry().addProvider(qgis.analysis.QgsNativeAlgorithms())

poiFile = r'C:\PSU\geog489\lesson4\assignment2Data\OSMpoints.shp' 
countryFile = r'C:\PSU\geog489\lesson4\assignment2Data\countries.shp' 
pointOutputFile = r'C:\PSU\geog489\lesson4\lessonData\pointsInCountry.shp' 
countryOutputFile = r'C:\PSU\geog489\lesson4\lessonData\singleCountry.shp' 

nameField = "NAME" 
countryName = "El Salvador"

output = processing.run("qgis:extractbyattribute", { "INPUT": countryFile, "FIELD": nameField, "OPERATOR": 0, "VALUE": countryName, "OUTPUT": countryOutputFile  }) 
print(output['OUTPUT'])

output = processing.run("native:clip", { "INPUT": poiFile, "OVERLAY": countryOutputFile, "OUTPUT": pointOutputFile }) 
print(output['OUTPUT']) 

qgs.exitQgis()