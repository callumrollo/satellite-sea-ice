import shutil
import requests
import pandas as pd
import numpy as np
from pathlib import Path
images_dir = Path("satellite_images")


def get_tif(datestamp, year_dir):
    month_str = datestamp.month_name().lower()[:3]
    date_str = str(datestamp).split(" ")[0]
    year, month, day = date_str.split("-")
    url = f'https://data.seaice.uni-bremen.de/amsr2/asi_daygrid_swath/s3125/{year}/{month_str}/Antarctic3125NoLandMask/asiNOLANDMASK-AMSR2-s3125-{year}{month}{day}-v5.4.tif'
    response = requests.get(url, stream=True)
    if response.status_code == 404:
        return
    with open(year_dir / f'{year}-{month}-{day}.tif', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


def main():
    if not images_dir.exists():
        images_dir.mkdir()
    for year in np.arange(2015, 2020):
        year_dir = images_dir / str(year)
        if not year_dir.exists():
            year_dir.mkdir()
        dates = list(pd.date_range(start=f'{year-1}-12-01', end=f'{year}-03-01', freq="1D"))
        for date in dates:
            get_tif(date, year_dir)


if __name__ == '__main__':
    main()