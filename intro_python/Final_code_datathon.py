import geopandas as gpd
import shapely
from shapely.geometry import Polygon

#add the WFS layer in geopandas
wfs_url = 'https://geoserver.geonet-mrn.de/xdatatogo/db_strecken/ows?service=WFS&version=2.0.0&request=GetFeature&typename=xdatatogo:db_strecken&outputFormat=json'
railway_layer = gpd.read_file(wfs_url)

# (1) clipping/ extracting the wfs layer based on user specified AOI
    ## get the user extent as bbox
user_extent = (8.002773139,9.316502057,49.253087351,50.566816268)
    ## create polygon from the bbox
aoi = Polygon([(user_extent[0], user_extent[1]), (user_extent[0], user_extent[3]),(user_extent[2], user_extent[3]), (user_extent[2], user_extent[1])])
    ## extract the geopandas object of WFS based on the bbox
extract_output = railway_layer[railway_layer.geometry.intersects(aoi)]
    ##create an empty shapefile
railway_layer_extract = "railway_layer_extract.shp"
    ##write the output from extract as a shapefile
extract_output.to_file(railway_layer_extract, driver='ESRI Shapefile')
print ('file extracting completed and saved as shapefile')



# (2) Reprojecting the extracted layer to EPSG:3857 in order to get 'metre' unit for buffering
    ## read the file a gpd 
railway_layer_extract = gpd.read_file("railway_layer_extract.shp")
print("Current CRS:", railway_layer_extract.crs)
    ## change the projection
railway_layer_extract_proj = railway_layer_extract.to_crs(epsg=3857)
print("Projected CRS:", railway_layer_extract_proj.crs)
   ##create an empty shapefile
output_reproj = 'railway_layer_extract_proj.shp'
    ##write the output from reprojection as a shapefile
railway_layer_extract_proj.to_file(output_reproj)
print ('layer reprojected')


# (3) creating a buffer of 200 m around the railway tracks
    ## read the file in geopandas
railway_layer_extract_proj = gpd.read_file('railway_layer_extract_proj.shp')
    ## specify the buffer distance
buffer_distance_m = 500
    ## buffering the layer using the user defined buffer distance
railway_layer_extract_proj['geometry'] = railway_layer_extract_proj['geometry'].buffer(buffer_distance_m)
    ## creating blank shapefile
output_buffer_shapefile = "railway_layer_extract_proj_buff.shp"
    ## writing the blank shapfefile with buffer output
railway_layer_extract_proj.to_file(output_buffer_shapefile, driver='ESRI Shapefile')
print ('layer buffer completed')


# (4) Identifying areas of foliage influence on railway network in autumn 
    ## getting the shapefiles into geopandas
intersect_input_1 = gpd.read_file('railway_layer_extract_proj_buff.shp')
intersect_input_2 = gpd.read_file('DLM_250_Forst.shp')
    ## Perform the intersection
#intersection_result = gpd.overlay(intersect_input_2, intersect_input_1, how='intersection')
clip_result = gpd.clip(intersect_input_1, intersect_input_2)
    ## Save the result to a new shapefile
output_file = 'railway_layer_intersect_forest.shp'
#intersection_result.to_file(output_file)
clip_result.to_file(output_file)
print('clip done')