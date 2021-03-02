import requests
import os.path
from pathlib import Path

def get_jhu_cached(date):
    formatted_date = date.strftime('%m-%d-%Y')
    path = f"./cache/jhu/{formatted_date}.csv"
    if not os.path.isfile(path):
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{formatted_date}.csv"
        r = requests.get(url, allow_redirects=True)
        open(path, 'wb').write(r.content)
    return path
