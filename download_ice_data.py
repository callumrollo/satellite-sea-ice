import shutil
import requests
import pandas as pd
import numpy as np
from pathlib import Path
import numpy as np

def get_tif(datestamp, year_dir):
    month_str = datestamp.month_name().lower()[:3]
    date_str = str(datestamp).split(" ")[0]
    year, month, day = date_str.split("-")
    url = f'https://data.seaice.uni-bremen.de/amsr2/asi_daygrid_swath/s3125/{year}/{month_str}/Antarctic3125NoLandMask/asiNOLANDMASK-AMSR2-s3125-{year}{month}{day}-v5.4.tif'
    print(url)
    #return
    response = requests.get(url, stream=True)
    if response.status_code == 404:
        return
    with open(f'images_daily_{year_dir}/{year}-{month}-{day}.tif', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    
for year in np.arange(2015, 2020):
    if not Path(f"images_daily_{year}").is_dir():
        Path(f"images_daily_{year}").mkdir()
    dates = list(pd.date_range(start=f'{year-1}-12-01', end=f'{year}-03-03', freq="1D"))
    for date in dates:
        get_tif(date, year)