# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import sys
import main
import configuration as config


params = config.postgres_params



def connectToPostgres(params):
    conn = None
    try:
        print("Connecting to postgresql...")
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("opened database succesfully !")
    return conn 


"""
"existStatus" shows its status if exists includes 
 its params:{‘fail’, ‘replace’, ‘append’} :
   fail: Raise a ValueError.
   replace: Drop the table before inserting new values.
   append: Insert new values to the existing table.
"""
def importToPostgres(params, tableName='wfs_test',existStatus="replace"):
    layerName = main.layerName
    url = main.url
    version_wfs = main.version_wfs
    outputCsvName = main.outputCsvName
    connectToPostgres(params)
    engine = create_engine(
        "postgresql://" + 
        params["user"] + ":" + 
        params["password"] + "@" +
        params["host"] + ":" +
        params["port"] + "/" +
        params["database"]
    )
    df = main.exportWFStToCSV(layerName, url, version_wfs, outputCsvName)
    df.to_sql(tableName, engine, if_exists=existStatus)
        
    
importToPostgres(params)



