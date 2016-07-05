import unittest

from bs4 import BeautifulSoup
import requests

from webscraper import *


class WebScraperTest(unittest.TestCase):
    """ Tests for web scraping components """

    def test_get_games_for_date(self):
        """ Test links returned against predefined games for Oct 8, 2015 """

        expected_games = ['/cfb/boxscores/2015-10-08-houston.html',
                          '/cfb/boxscores/2015-10-08-southern-california.html']
        self.assertEqual(expected_games, get_all_games_for_date(2015, 10, 8))

    def get_game_summary_info(self):
        pass

    def get_passing_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2016-01-11-clemson.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = ''  # TODO: add item for test
        self.assertIn(expected_item, get_passing_stats(content))

    def get_rush_receive_stats(self):
        pass

    def get_defense_stats(self):
        pass

    def get_return_stats(self):
        pass

    def get_kick_punt_stats(self):
        pass
