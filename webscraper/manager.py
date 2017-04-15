""" Used to keep track of state during scraping process """

import re
from collections import namedtuple
from uuid import uuid4
from datetime import date

import requests
from bs4 import BeautifulSoup


class ScrapingManager:
    """ Manages the state and relationship with database for web scraping """

    __url_root = 'http://sports-reference.com'

    # TODO:  Add namedtuple to server as data containers for each scraped component
    # PlayerContainer = namedtuple('PlayerContainer' ['Id', 'Name'])  # TODO: finish values

    def __init__(self, db):
        """ Instantiates an object of Scraping Manager """

        self.db = db

        # TODO: make sure these are represented as dictionaries
        # Represented as key -> (name, link) | value -> {'id': uuid4, 'years': []}
        # self.teams = self.db.select_all_from_table('Team')

        # Represented as key -> (name, link) | value -> uuid4
        # self.players = self.db.select_all_from_table('Player')
        # self.conferences = self.db.select_all_from_table('Conference')

        # self.last_date = self.db.execute_query('SELECT MAX(GameDate) FROM Game')

        self.staged_data = list()

    @staticmethod
    def generate_id(): return uuid4()

    def get_or_make_id(self, source, value):
        """ Checks for existing id value in mapped stores (ex. self.teams) and either
            returns existing value or returns a newly generated one """

        existing = getattr(self, source)
        if value not in existing.get(value):
            return self.generate_id()
        else:
            return existing[value]

    def commit_staged_data(self):
        """ Take manager's staged data and insert into database """

        for key, val in self.staged_data.items():
            self.db.add_rows_to_table(key, val)

        self.staged_data = None

    @staticmethod
    def filter_html_list(items):
        """ Takes list of html from scraping and removes unnecessary elements """
        return list(filter(lambda x: x != '\n', items))

    @staticmethod
    def extract_components_from_html(html_list):
        """ Updates list of html elements with desired statistical components """

        for idx, value in enumerate(html_list):
            if value.get('href'):
                html_list[idx] = (value.string, value['href'])
            elif value.find('a'):
                html_list[idx] = (value.find('a').string, value.find('a')['href'])
            else:
                html_list[idx] = value.find(text=lambda y: y != '\n',
                                            recursive=False) if value.contents else 0
        return html_list

    @staticmethod
    def get_table_container(content, text):
        """ Uses heading text from DOM to retrieve tabular html content """
        return content.find('h2', text=text).parent.findNextSibling()

    @staticmethod
    def get_all_games_for_date(in_date=date.today()):
        """ Retrieves links for all games occurring on a specified date """

        if date.today() <= in_date:
            raise ValueError("Must provide past date")

        url = str.format('{0}/cfb/boxscores/index.cgi?month={1}&day={2}&year={3}',
                         ScrapingManager.__url_root, in_date.month, in_date.day,
                         in_date.year)

        soup = BeautifulSoup(requests.get(url).content, 'lxml')
        regex_string = str.format('.*{}.*', in_date.strftime('%Y-%m-%d'))
        return [link.get('href') for link
                in soup.find_all('a', href=re.compile(regex_string), text='Final')]

    @staticmethod
    def get_game_summary_info(content, link):
        """ Retrieves game score and summary info for specified link """

        teams = [(x.string, x['href']) for x in content.find('h1').find_all('a')]
        scores = re.findall(r"[0-9]\w+", content.find('h1').text)

        # TODO: convert team names into id values

        return tuple([link, teams[0], scores[0], teams[1], scores[1]])

    @staticmethod
    def get_game_team_stats(content):
        """ Retrieves team-level box score data for specified game """

        team_stats = list()

        # Teams
        team_stats.append([x for x in content.find_all('a', href=re.compile('.*schools/.+'))[:2]])
        # TODO: convert team names into id values

        # Play/Yardage Statistics
        team_stats.append([x for x in content.find(text='Total Yards').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Total Plays').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Yds/Play').parent.next_siblings if x != '\n'])

        # First Down Statistics
        team_stats.append([x for x in content.find(text='First Downs').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Pass').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Rush').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Penalty').parent.next_siblings if x != '\n'])

        # Penalty Statistics
        team_stats.append([x for x in content.find(text='Penalties').parent.next_siblings if x != '\n'])
        team_stats.append([x for x in content.find(text='Yds').parent.next_siblings if x != '\n'])

        team_stats = [list(x) for x in zip(*team_stats)]

        return [tuple(ScrapingManager.extract_components_from_html(x)) for x in team_stats]

    @staticmethod
    def get_passing_stats(content):
        """ Retrieves player-level passing data for specified game """

        header = ScrapingManager.get_table_container(content, 'Passing')
        html = [x.parent.parent.contents
                for x in header.find_all('a', href=re.compile('.*player.*'))]

        # TODO: convert player names into id values

        return [tuple(ScrapingManager.extract_components_from_html(x))
                for x in map(ScrapingManager.filter_html_list, html)]

    @staticmethod
    def get_rush_receive_stats(content):
        """ Retrieves player-level rush and receiving data for specified game """

        header = ScrapingManager.get_table_container(content, 'Rushing & Receiving')
        html = [x.parent.parent.contents
                for x in header.find_all('a', href=re.compile('.*player.*'))]

        # TODO: convert player names into id values

        return [tuple(ScrapingManager.extract_components_from_html(x))
                for x in map(ScrapingManager.filter_html_list, html)]

    @staticmethod
    def get_defense_stats(content):
        """ Retrieves player-level defensive data for specified game """

        header = ScrapingManager.get_table_container(content, 'Defense & Fumbles')
        html = [x.parent.parent.contents
                for x in header.find_all('a', href=re.compile('.*player.*'))]

        # TODO: convert player names into id values

        return [tuple(ScrapingManager.extract_components_from_html(x))
                for x in map(ScrapingManager.filter_html_list, html)]

    @staticmethod
    def get_return_stats(content):
        """ Retrieves player-level punt/kick return data for specified game """

        header = ScrapingManager.get_table_container(content, 'Kick & Punt Returns')
        html = [x.parent.parent.contents
                for x in header.find_all('a', href=re.compile('.*player.*'))]
        return [tuple(ScrapingManager.extract_components_from_html(x))
                for x in map(ScrapingManager.filter_html_list, html)]

    @staticmethod
    def get_kick_punt_stats(content):
        """ Retrieve player-level kicking data for specified game """

        header = ScrapingManager.get_table_container(content, 'Kicking & Punting')
        html = [x.parent.parent.contents
                for x in header.find_all('a', href=re.compile('.*player.*'))]

        # TODO: convert player names into id values

        return [tuple(ScrapingManager.extract_components_from_html(x))
                for x in map(ScrapingManager.filter_html_list, html)]

    def execute_game_data_collection(self, link):
        """ Function used to collect game data for specified link """

        page_content = BeautifulSoup(requests.get(link).content, 'lxml')

        for e in page_content.find_all('br'):
            e.replace_with('')

        gsi = ScrapingManager.get_game_summary_info(page_content)
        gts = ScrapingManager.get_game_team_stats(page_content)
        ps = ScrapingManager.get_passing_stats(page_content)
        rrs = ScrapingManager.get_rush_receive_stats(page_content)
        ds = ScrapingManager.get_defense_stats(page_content)
        rs = ScrapingManager.get_return_stats(page_content)
        kps = ScrapingManager.get_kick_punt_stats(page_content)

        # TODO: need to handle new teams and players

        self.staged_data.extend(gsi + gts + ps + rrs + ds + rs + kps)

    @staticmethod
    def get_conference_details():
        pass

    @staticmethod
    def get_conference_affiliation(team, year):
        """ Generates a conference affiliation record for given team and year """

        soup = BeautifulSoup(requests.get(str.format('{0}/{1}.html', team[1], year)).content, 'lxml')
        item = soup.find('a', href=re.compile('.*conferences/.+'))

        # TODO: return as namedtuple

        return item