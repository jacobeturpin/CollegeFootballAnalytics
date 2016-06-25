import unittest
from .test_webscraper import WebScraperTest


def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WebScraperTest))
    return suite