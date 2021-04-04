

wfs_params = {
    "url": "http://localhost:8080/geoserver/topp/wfs",
    "version_wfs" : "1.1.0",
    "layerName" : "topp:states",
    "outputCsvName" : "test_wfs.csv"
}


postgres_params = {
    "host" : "localhost",
    "port" : "5432",
    "database" : "postgres",
    "user": "postgres",
    "password" : "2416",
}


mssql_params = {
    "server": "(localdb)\MSSQLLocalDB",
    "database" : "Poligonlar",
    "outputTableName" : "test_wfs"   
}
