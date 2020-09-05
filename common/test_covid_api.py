import unittest
import datetime as dt
from .covid_api import *

class TestCovidAPI(unittest.TestCase):
    def test_get_all_countries(self):
        countries = get_all_countries()
        self.assertNotEqual(len(countries), 0)

    def test_get_live_country_info(self):
        start = dt.date.today() - dt.timedelta(days=3)
        end = dt.date.today() - dt.timedelta(days=1)
        df = get_live_country_info('south-africa', start, end)
        self.assertNotEqual(0, len(df))
        self.assertIn('Country', df.columns)
        self.assertIn('Cases', df.columns)
        self.assertIn('Date', df.columns)
        self.assertEqual(len(df),(end-start).days + 1)