# -*- coding: utf-8 -*-
# 
from owslib.wfs import WebFeatureService
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pyodbc
import urllib
import configuration as config 


url = config.wfs_params["url"]
version_wfs = config.wfs_params["version_wfs"]
layerName = config.wfs_params["layerName"]
outputCsvName = config.wfs_params["outputCsvName"]



def GetInfoFromWFS(url, version):
    wfs = WebFeatureService( url = url, version = version_wfs )
    
    sortedLayerIds= list( sorted(wfs.contents.keys()) )

    for layerId in sortedLayerIds[0: len(sortedLayerIds)]:
        layer = wfs[layerId]
        print('Layer Id: ', layerId)
        print('Title:', layer.title)
        print("CRS: ", layer.crsOptions)
        print('Boundaries as WGS84:', layer.boundingBoxWGS84)
        print('Properties: ', list( wfs.get_schema( layerId )['properties'].keys() ) )
        print('Geometry type: ',  wfs.get_schema( layerId )['geometry'])
        print('Geometry_column: ',  wfs.get_schema( layerId )['geometry_column'] , "\n" )
    return wfs
    

def exportWFStToCSV(layerName, url, version_wfs, outputCsvName="test_wfs.csv"):
    wfs = GetInfoFromWFS(url, version_wfs)
    layerId = layerName
    content = wfs.contents[layerId]
    print('Selected layer title: ', content.title)
    
    exportData = wfs.getfeature(typename = layerId, outputFormat='csv')
    outputCsvName = outputCsvName
    with open(outputCsvName, 'wb') as fh:
        fh.write(exportData.read())
    
    df = pd.read_csv(outputCsvName)
    return df


# exportWFStToCSV(layerName,url,version_wfs, "test_wfs.csv")


