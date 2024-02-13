# Intro R

## Ressources

+ [Tutorial: Using WFS services in R](https://inbo.github.io/tutorials/tutorials/spatial_wfs_services/)
+ [Simple WGS reference (GeoServer)](https://docs.geoserver.org/stable/en/user/services/wfs/reference.html)
+ [Book: Geocomputation with R](https://r.geocompx.org/)
+ [ows4R reference](https://eblondel.github.io/ows4R/index.html)
+ [sf reference](https://r-spatial.github.io/sf/index.html)
+ [tmap reference](https://r-tmap.github.io/tmap/index.html)

## Configuration issues

    IOPub data rate exceeded.
    The Jupyter server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--ServerApp.iopub_data_rate_limit`.

    Current values:
    ServerApp.iopub_data_rate_limit=1000000.0 (bytes/sec)
    ServerApp.rate_limit_window=3.0 (secs)

`jupyter server --generate-config`  
In `~/.jupyter/jupyter_server_config.py` set
    c.ZMQChannelsWebsocketConnection.iopub_data_rate_limit = 10000000

---------


  