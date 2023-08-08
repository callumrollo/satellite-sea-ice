# satellite-sea-ice

Download geotiffs of satellite ice data and extract the ice concentration at specified locations

`download_ice_data.py` will download the geotiffs (no land mask) for a user specified range of dates

`classify_ice.ipynb` reads the geotiffs and extracts the nearest pixel to usere specified lon-lat pairs and plots the sea ice extent in time

`figures` contains two figures: the ice cover percentage and whether each day is classed as open water (ice <= 50 %) or ice (ice > 50 %)
