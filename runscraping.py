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

    # TODO: get games on current date

    # TODO: scrape games occurring on current date

    # TODO: add data to database

    sleep(3600 * 4)  # Wait four hours
