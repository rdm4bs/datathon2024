# Using R in a Jupyter Notebook

Install [R-kernel for JupyterLab](https://irkernel.github.io/installation/).

**Dependencies**

+ [sf](https://cran.r-project.org/web/packages/sf/index.html)
+ [stars](https://cran.r-project.org/web/packages/stars/index.html)
+ [terra](https://cran.r-project.org/web/packages/terra/index.html)
+ [ows4r](https://cran.r-project.org/web/packages/ows4R/index.html)
+ [tmap](https://cran.r-project.org/web/packages/tmap/index.html)

## Resources

+ [Tutorial: Using WFS services in R](https://inbo.github.io/tutorials/tutorials/spatial_wfs_services/)
+ [Simple WFS reference (GeoServer)](https://docs.geoserver.org/stable/en/user/services/wfs/reference.html)
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