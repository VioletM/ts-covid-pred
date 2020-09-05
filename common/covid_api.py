import requests
import json
import logging
import sys
import datetime

import pandas as pd


logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)-15s [%(name)s::%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler(sys.stdout),
            ]
        )
logger = logging.getLogger(__name__)


def get_all_countries():
    url = 'https://api.covid19api.com/countries'
    resp = requests.get(url)
    if resp.status_code == 200:
        countries = [{item["Slug"]: item["Country"]} for item in resp.json()]
        logger.info(f"Countries number: {len(countries)}")
        return countries
    else:
        raise RuntimeError(f"Can't get all countries. {resp.status_code}: {resp.reason}")

def get_live_country_info(slug: str, start: datetime.date, end: datetime.date):
    start = start.isoformat()
    end = end.isoformat()
    url = f'https://api.covid19api.com/country/{slug}/status/confirmed/live?from={start}&to={end}'
    resp = requests.get(url)
    if resp.status_code == 200:
        df = pd.DataFrame(resp.json())
        logger.info(f"Get data for {slug}")
        return df
    else:
        logger.error(f"Can't get info for {slug}, because {resp.status_code}: {resp.reason}")
        return pd.DataFrame(columns=['Country', 'Cases', 'Date'])

