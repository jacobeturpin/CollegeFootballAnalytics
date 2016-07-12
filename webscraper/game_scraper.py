""" Functional module to scrape web data """

from datetime import date, timedelta

from bs4 import BeautifulSoup
import requests
import re


__url_root = 'http://sports-reference.com'


def filter_html_list(items):
    """ Takes list of html from scraping and removes unnecessary elements """
    return list(filter(lambda x: x != '\n', items))


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


def get_table_container(content, text):
    """ Uses heading text from DOM to retrieve tabular html content """
    return content.find('h2', text=text).parent.findNextSibling()


def get_all_games_for_date(year, month, day):
    """ Retrieves links for all games occurring on a specified date """

    input_date = date(month=month, day=day, year=year)

    if date.today() <= input_date:
        raise ValueError("Must provide past date")

    url = str.format('{0}/cfb/boxscores/index.cgi?month={1}&day={2}&year={3}',
                     __url_root, month, day, year)

    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    regex_string = str.format('.*{}.*', input_date.strftime('%Y-%m-%d'))
    return [link.get('href') for link 
            in soup.find_all('a', href=re.compile(regex_string), text='Final')]


def get_game_summary_info(content, link):
    """ Retrieves game score and summary info for specified link """

    teams = [(x.string, x['href']) for x in content.find('h1').find_all('a')]
    scores = re.findall(r"[0-9]\w+", content.find('h1').text)

    return (link, teams[0], scores[0], teams[1], scores[1])


def get_game_team_stats(content):
    """ Retrieves team-level box score data for specified game """

    team_stats = list()

    # Teams
    team_stats.append([x for x in content.find_all('a', href=re.compile('.*schools/.+'))[:2]])

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

    return [tuple(extract_components_from_html(x)) for x in team_stats]


def get_passing_stats(content):
    """ Retrieves player-level passing data for specified game """

    header = get_table_container(content, 'Passing')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return [tuple(extract_components_from_html(x)) for x in map(filter_html_list, html)]


def get_rush_receive_stats(content):
    """ Retrieves player-level rush and receiving data for specified game """
    
    header = get_table_container(content, 'Rushing & Receiving')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return [tuple(extract_components_from_html(x)) for x in map(filter_html_list, html)]


def get_defense_stats(content):
    """ Retrieves player-level defensive data for specified game """
    
    header = get_table_container(content, 'Defense & Fumbles')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return [tuple(extract_components_from_html(x)) for x in map(filter_html_list, html)]


def get_return_stats(content):
    """ Retrieves player-level punt/kick return data for specified game """
    
    header = get_table_container(content, 'Kick & Punt Returns')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return [tuple(extract_components_from_html(x)) for x in map(filter_html_list, html)]


def get_kick_punt_stats(content):
    """ Retrieve player-level kicking data for specified game """
    
    header = get_table_container(content, 'Kicking & Punting')
    html = [x.parent.parent.contents for x in header.find_all('a', href=re.compile('.*player.*'))]
    return [tuple(extract_components_from_html(x)) for x in map(filter_html_list, html)]


def execute_game_data_collection(link):
    """ Function used to collect game data for specified link """

    page_content = BeautifulSoup(requests.get(link).content, 'lxml')

    for e in page_content.find_all('br'):
        e.replace_with('')

    gsi = get_game_summary_info(page_content)
    gts = get_game_team_stats(page_content)
    ps = get_passing_stats(page_content)
    rrs = get_rush_receive_stats(page_content)
    ds = get_defense_stats(page_content)
    rs = get_return_stats(page_content)
    kps = get_kick_punt_stats(page_content)
    return gsi, gts, ps, rrs, ds, rs, kps


if __name__ == '__main__':
    """ Perform data capture for the current date """
    
    yestr = date.today() - timedelta(days=1)
    games = get_all_games_for_date(year=yestr.year, month=yestr.month, day=yestr.day)
    for game in games:
        execute_game_data_collection(game)
