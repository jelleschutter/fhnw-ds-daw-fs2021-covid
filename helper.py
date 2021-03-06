import requests
import os.path
from pathlib import Path
from bokeh.plotting import gridplot

def get_jhu_cached(date):
    formatted_date = date.strftime('%m-%d-%Y')
    path = f"./cache/jhu/{formatted_date}.csv"
    if not os.path.isfile(path):
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{formatted_date}.csv"
        r = requests.get(url, allow_redirects=True)
        open(path, 'wb').write(r.content)
    return path

def create_grid(graphs, columns=6, **kwargs):
    grid = []
    current_row = []
    i = 1
    for graph in graphs:
        current_row.append(graph)
        if i % columns == 0:
            grid.append(current_row)
            current_row = []
        i += 1
    if len(current_row) > 0:
        grid.append(current_row)
    return gridplot(grid, **kwargs)
