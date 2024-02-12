import geopandas as gpd
import requests
import shapely

# Add the WFS layer in geopandas
# Specify the base WFS url of the service
railway_wfs_url = 'https://geoserver.geonet-mrn.de/xdatatogo/db_strecken/ows'

# Specify HTTP GET parameters
railway_wfs_params = dict(
    service='WFS',
    request='GetFeature',
    typeNames='xdatatogo:db_strecken',
    outputFormat='json',
)

# Build the request by adding all parameters to the service URL
request = requests.Request('GET', railway_wfs_url, params=railway_wfs_params).prepare()
railway_network = gpd.read_file(request.url)

# Clip the wfs layer based on user specified AOI
bbox = shapely.envelope(
    shapely.MultiPoint([(6.345854, 51.295232), (11.598078, 54.13791)])
)
railway_network = railway_network.clip(bbox)


# Reproject the extracted layer to EPSG:25832 in order to get 'metre' unit for buffering
print('Previous CRS:', railway_network.crs)
railway_network = railway_network.to_crs(epsg=25832)
print('New CRS:', railway_network.crs)

# Create a buffer of 20 m around the railway tracks
buffer_distance_m = 20

# Duplicate layer to separately store it with a buffered geometry
railway_network_buffer = railway_network.copy()
railway_network_buffer['geometry'] = railway_network['geometry'].buffer(buffer_distance_m)


# Identify areas of foliage influence on railway network
# Add reference system identifier to bbox parameter
bbox_parameter = ','.join(str(coord) for coord in bbox.bounds) + ',EPSG:4326'

forest_wfs_url = 'https://sgx.geodatenzentrum.de/wfs_dlm250'
forest_wfs_params = dict(
    service='WFS',
    request='GetFeature',
    typeNames='dlm250:objart_43002_f',
    outputFormat='json',
    bbox=bbox_parameter
)
request = requests.Request('GET', forest_wfs_url, params=forest_wfs_params).prepare()
forest_patches = gpd.read_file(request.url)

# Perform spatial intersection
result = gpd.overlay(railway_network_buffer, forest_patches, how='intersection')

output_file = 'railway_network_intersect_forest.json'
result.to_file(output_file)
print('File exported successfully.')