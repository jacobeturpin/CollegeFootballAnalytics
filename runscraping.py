""" Module used to contain logic for main loop used to populate database with
    scraped data at regular intervals"""

from time import sleep
from datetime import date

from database import DatabaseManager
from webscraper import ScrapingManager

db = DatabaseManager()
scraper = ScrapingManager(db)

while True:
    """ Open loop to record daily statistics """

    today = date.now()

    games = scraper.get_all_games_for_date(today.year, today.month, today.day)

    for game in games:
        scraper.execute_game_data_collection(game)

    scraper.commit_staged_data()

    sleep(3600 * 4)  # Wait four hours
