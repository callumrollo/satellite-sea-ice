# satellite-sea-ice

Download geotiffs of satellite ice data and extract the ice concentration at specified locations

`download_ice_data.py` will download the geotiffs (no land mask) for a user specified range of dates

`classify_ice.ipynb` reads the geotiffs and extracts the nearest pixel to user specified lon-lat pairs and plots the sea ice extent in time

`results` contains csv files of ice percentage and classification for the user specified sites and time range

`figures` contains figures from the results
