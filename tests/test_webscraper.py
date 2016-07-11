import unittest

from webscraper import *


class WebScraperTest(unittest.TestCase):
    """ Tests for web scraping components """

    def test_get_all_games_for_date(self):
        """ Test links returned against predefined games for Oct 8, 2015 """

        expected_games = ['/cfb/boxscores/2015-10-08-houston.html',
                          '/cfb/boxscores/2015-10-08-southern-california.html']
        self.assertEqual(expected_games, get_all_games_for_date(2015, 10, 8))

    def test_get_game_summary_info(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2000-09-16-akron.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = ('/cfb/boxscores/2000-09-16-akron.html',
                         ('Central Florida', '/cfb/schools/central-florida/2000.html'), 24,
                         ('Akron', '/cfb/schools/akron/2000.html'), 35)
        self.assertIn(expected_item, get_game_summary_info(content))

    def test_get_game_team_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2003-09-11-utah.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')

        for e in content.find_all('br'):
            e.replace_with('')

        expected_item = [(('California', '/cfb/schools/california/2003.html'), '365', '66', '5.5', '19', '13',
                         '5', '1', '2', '10'),
                         (('Utah', '/cfb/schools/utah/2003.html'), '336', '76', '4.4', '21', '7', '14', '0',
                         '7', '52')]
        self.assertEquals(expected_item, get_game_team_stats(content))

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
        link = 'http://www.sports-reference.com/cfb/boxscores/2006-10-14-louisiana-tech.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = (('Ben Alexander', '/cfb/players/ben-alexander-1.html'),
                         ('Idaho', '/cfb/schools/idaho/2006.html'),
                         '0', '4', '4', '0.0', '0.0', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertIn(expected_item, get_defense_stats(content))

    def test_get_return_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2009-11-11-central-michigan.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = (('Antonio Brown', '/cfb/players/antonio-brown-1.html'),
                         ('Central Michigan', '/cfb/schools/central-michigan/2009.html'),
                         '4', '68', '17.0', '0', 0, 0, 0, 0)
        self.assertIn(expected_item, get_return_stats(content))

    def test_get_kick_punt_stats(self):
        link = 'http://www.sports-reference.com/cfb/boxscores/2013-12-07-arizona-state.html'
        content = BeautifulSoup(requests.get(link).content, 'lxml')
        expected_item = (('Alex Garoutte', '/cfb/players/alex-garoutte-1.html'),
                         ('Arizona State', '/cfb/schools/arizona-state/2013.html'),
                         0, 0, 0, 0, 0, 0, 0, '4', '132', '33.0')
        self.assertIn(expected_item, get_kick_punt_stats(content))


if __name__ == '__main__':
    unittest.main()
