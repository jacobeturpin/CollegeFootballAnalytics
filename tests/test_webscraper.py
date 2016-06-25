import unittest
from webscraper import *

class WebScraperTest(unittest.TestCase):
    """ Tests for web scraping components """

    def test_get_games_for_date(self):

        expected_games = ['/cfb/boxscores/2015-10-08-houston.html',
                          '/cfb/boxscores/2015-10-08-southern-california.html']

        self.assertEqual(expected_games, get_all_games_for_date(2015, 10, 8))

