import unittest

from webscraper import *


class WebScraperTest(unittest.TestCase):
    """ Tests for web scraping components """

    def test_get_games_for_date(self):
        """ Test links returned against predefined games for Oct 8, 2015 """

        expected_games = ['/cfb/boxscores/2015-10-08-houston.html',
                          '/cfb/boxscores/2015-10-08-southern-california.html']
        self.assertEqual(expected_games, get_all_games_for_date(2015, 10, 8))

    def test_get_game_summary_info(self):
        pass

    def test_get_game_team_stats(self):
        pass

    def test_get_passing_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2016-01-11-clemson.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = (('Deshaun Watson', '/cfb/players/deshaun-watson-1.html'),
                         ('Clemson', '/cfb/schools/clemson/2015.html'),
                         '30', '47', '63.8', '405', '8.6', '9.4', '4', '1', '160.0')
        self.assertIn(expected_item, get_passing_stats(content))

    def test_get_rush_receive_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2012-10-11-troy.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = (('Antonio Andrews', '/cfb/players/antonio-andrews-1.html'),
                         ('Western Kentucky', '/cfb/schools/western-kentucky/2012.html'),
                         '26', '113', '4.3', '0', '1', '14', '14.0', '0', '27', '127', '4.7', '0')
        self.assertIn(expected_item, get_rush_receive_stats(content))

    def test_get_defense_stats(self):
        pass

    def test_get_return_stats(self):
        pass

    def test_get_kick_punt_stats(self):
        pass


if __name__ == '__main__':
    unittest.main()
