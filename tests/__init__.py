import unittest

from .test_webscraper import GameScraperTest


def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GameScraperTest))
    return suite
