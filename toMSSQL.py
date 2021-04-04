# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import urllib
import sys
import main
import configuration as config

"""
for MSSQL Server using  windows Authentication
namely, it is not appropriate for SQL Server Authentication (it will develop later! )
"""

params = config.mssql_params


"""
"existStatus" shows its status if exists includes 
 its params:{‘fail’, ‘replace’, ‘append’} :
   fail: Raise a ValueError.
   replace: Drop the table before inserting new values.
   append: Insert new values to the existing table.
"""
def importToMSSQL(params,tableName='wfs_test', existStatus="replace"):
    layerName = main.layerName
    url = main.url
    version_wfs = main.version_wfs
    outputCsvName = main.outputCsvName
    tableName = params["outputTableName"]
    
    quoted = urllib.parse.quote_plus(
        "DRIVER={SQL Server Native Client 11.0};SERVER="+
        params["server"]+
        ";DATABASE="
        +params["database"]
    )
    engine_sqlserver = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    df = main.exportWFStToCSV(layerName, url, version_wfs, outputCsvName)
    df.to_sql(tableName, schema='dbo', con=engine_sqlserver, if_exists=existStatus)

importToMSSQL(params, existStatus="replace")