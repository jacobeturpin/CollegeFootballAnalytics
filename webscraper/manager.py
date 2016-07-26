""" Used to keep track of state during scraping process """

import re
import requests
from uuid import uuid4
from datetime import date

from bs4 import BeautifulSoup


class ScrapingManager:
    """ Manages the state and relationship with database for web scraping """

    __url_root = 'http://sports-reference.com'

    def __init__(self, db):
        """ Instantiates an object of Scraping Manager """

        self.db = db

        self.teams = db.select_all_from_table('Team')
        self.players = db.select_all_from_table('Player')
        self.conferences = db.select_all_from_table('Conference')

        self.last_date = db.execute_query('SELECT MAX(GameDate) FROM Game')

        self.staged_data = None

    def generate_id(self): return uuid4()

    def check_vals_for_id(self):
        pass

    @staticmethod
    def get_all_games_for_date(year, month, day):
        """ Retrieves links for all games occurring on a specified date """

        input_date = date(month=month, day=day, year=year)

        if date.today() <= input_date:
            raise ValueError("Must provide past date")

        url = str.format('{0}/cfb/boxscores/index.cgi?month={1}&day={2}&year={3}',
                         ScrapingManager.__url_root, month, day, year)

        soup = BeautifulSoup(requests.get(url).content, 'lxml')
        regex_string = str.format('.*{}.*', input_date.strftime('%Y-%m-%d'))
        return [link.get('href') for link
                in soup.find_all('a', href=re.compile(regex_string), text='Final')]

