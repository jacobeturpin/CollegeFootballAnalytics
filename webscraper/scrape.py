""" Functional script to scrape web data """

from datetime import date

from bs4 import BeautifulSoup
import requests
import re


__url_root = 'http://sports-reference.com/cfb/'


def clean_html(item):
   """ Takes html from scraping and removes unecessary elements """
   return list(filter(lambda x: x != '\n', item))

def extract_components_from_html(list):
    pass

def get_table_container(content, text):
    """ Uses heading text from DOM to retrieve tabular html content """
    return content.find('h2', text=text).parent.findNextSibling()

def get_all_games_for_date(year, month, day):
    """ Retrieves links for all games ocurring on a specified date """

    if date.today() < date(month=month, day=day, year=year):
        raise ValueError("Must use past date")

    url = str.format('{0}boxscores/index.cgi?month={1}&day={2}&year={3}',
                     __url_root, month, day, year)

    page_content =  requests.get(url).content
    soup = BeautifulSoup(page_content, "html.parser")
    table = get_table_container(soup, text=re.compile('[0-9]+ Game.*'))
    return [link.get('href') for link in table.find_all('a', text='Final')]

def get_game_summary_info(content):
    """ Retrieves game score and summary info for specified link """
    pass

def get_game_team_stats(content):
    """ Retrieves team-level box score data for specified game """
    pass

def get_passing_stats(content):
    """ Retrieves player-level passing data for specified game """

    header = get_table_container(content, 'Passing')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return list(map(clean_html, html))

def get_rush_receive_stats(content):
    """ Retrieves player-level rush and receiving data for specified game """
    
    header = get_table_container(content, 'Rushing & Receiving')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return list(map(clean_html, html))

def get_defense_stats(content):
    """ Retrieves player-level defensive data for specified game """
    
    header = get_table_container(content, 'Defense & Fumbles')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return list(map(clean_html, html))

def get_return_stats(content):
    """ Retrieves player-level punt/kick return data for specified game """
    
    header = get_table_container(content, 'Kick & Punt Returns')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return list(map(clean_html, html))

def get_kick_punt_stats(content):
    """ Retrieve player-level kicking data for specified game """
    
    header = get_table_container(content, 'Kicking & Punting')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return list(map(clean_html, html))

def execute_game_data_collection(link):
    """ Function used to collect game data for specified link """
    page_content = BeautifulSoup(requests.get(link).content, 'html.parser')
    gsi = get_game_summary_info(page_content)
    gts = get_game_team_stats(page_content)
    ps = get_passing_stats(page_content)
    rrs = get_rush_receive_stats(page_content)
    ds = get_defense_stats(page_content)
    rs = get_return_stats(page_content)
    kps = get_kick_punt_stats(page_content)
    return gsi, gts, ps, rrs, ds, rs, kps
