""" Functional script to scrape web data """

import bs4
import requests


__url_root = 'http://sports-reference.com/cfb/'


def get_all_games_for_date(year, month, day):
    """ Retrieves links for all games ocurring on a specified date """
    pass

def get_game_summary_info(content):
    """ Retrieves game score and summary info for specified link """
    pass

def get_game_team_stats(content):
    """ Retrieves team-level box score data for specified game """
    pass

def get_passing_stats(content):
    """ Retrieves player-level passing data for specified game """
    pass

def get_rush_receive_stats(content):
    """ Retrieves player-level rush and receiving data for specified game """
    pass

def get_defense_stats(content):
    """ Retrieves player-level defensive data for specified game """
    pass

def get_return_stats(content):
    """ Retrieves player-level punt/kick return data for specified game """
    pass

def get_kick_punt_stats(content):
    """ Retrieve player-level kicking data for specified game """
    pass

def execute_game_data_collection(link):
    """ Function used to collect game data for specified link """
    with requests.get(link).content as page_content:
        gsi = get_game_summary_info(page_content)
        gts = get_game_team_stats(page_content)
        ps = get_passing_stats(page_content)
        rrs = get_rush_receive_stats(page_content)
        ds = get_defense_stats(page_content)
        rs = get_return_stats(page_content)
        kps = get_kick_punt_stats(page_content)
    return gsi, gts, ps, rrs, ds, rs, kps
