# Data story ideas

## Ideas from Datathon organisers

- Determine agricultural emissions for region of Braunschweig over time
  - Include emission variation over time (the TI layers below are time series data) and plot a graph.
  - Compare these agricultural emmissions with emissions from traffic. Search for appropriate data.
  - Datasets
    + [Emissionen von Treibhausgasen der deutschen Landwirtschaft WFS](https://atlas.thuenen.de/layers/geonode_data_ingest:geonode:emissionen_lawi_1990_2021_thg)
    + [Emissionen von Luftschadstoffen der deutschen Landwirtschaft WFS](https://atlas.thuenen.de/layers/geonode_data_ingest:geonode:emissionen_lawi_1990_2021_luftschadstoffe)
  - Example SQL filter to get features for Braunschweig (ID 3101):  
`SELECT * FROM emissionen_lawi_1990_2021_luftschadstoffe WHERE d_id = 3101`

- How has forest land use changed between 2005 and 2011?
  - A simple change detection between 2 layers.

- What is the distribution of different forest inventory in your region of interest?
  - Summarize wood stocks/wood reserves for your region of interest.
  - E.g.: difference between predominant tree species in Harz mountains and northern Braunschweig (Heide).

- How is the water balance over time in your region of interest?
  - Time series evaluation of water balance in your choice of forest area.

## Ideas from participants

### Ecology

- Korrelation von Lichtverschmutzung mit Vogelzugverhalten in Europa
  - NANA/NOAA composite "Earth's City Lights"
- Fischotter-Totfunde in Mecklenburg-Vorpommern: Hauptsächlich an Straßen oder an Gewässern?

### Forest, agriculture and topography

- Vergleich von Harz und Rothaargebirge hinsichtlich Baumarten und -bestand
- Zerschneidung zusammenhängender Naturräume durch Straßen in Deutschland
- Forest fires: Determine correlation of susceptibility to burning with tree species
- Raum-zeitliche Darstellung von Treibhausgas- und Schadstoffemissionen aus der Landwirtschaft
- 3D rendering of tree canopy height from Sentinel data for Niedersachsen with R 

### Urban, social and demographic

- Zugänglichkeit von Grünflächen in Braunschweig korreliert mit Bevölkerungsdichte einzelner Wohnquartiere
- Wohnraumentwicklung in Düsseldorf, Verknüpfung statistischer Daten mit räumlichen Features (Bündnis für bezahlbaren Wohnraum)
  - Mit Geocoding via Nominatim in QGIS
- Hannover: Welche Gebäude waren vom vergangenen Hochwasser betroffen?
  - Verschneidung von OSM-Gebäudedaten mit Sentinel-Radarsatellitendaten (SAR)

### Transport and mobility

- Dichtekarte des Hauptflugverkehrs über dem Nordatlantik
- Variation of railway network exposure to foliage by wind influence
- Extending our railway foliage story with train speeds and creating a convincing visualisation in QGIS for further reasoning

### Geological time scales/planetary

- Visualisierung tektonischer Plattenbewegung anhand unterschiedlicher Simulationsmodelle
- Raum-zeitliche Darstellung von Kaltzeiten/Eisbedeckung/Vulkanismus
