""" A simple tool to scrape college football statistics
    for analysis
"""

from configparser import ConfigParser

from server import app


def run_debug_server():
    """ Test """

    config = ConfigParser()

    config['DATABASE'].get('server')

    app.run('0.0.0.0', debug=True)
    return None


if __name__ == '__main__':
    print('Testing main')
    run_debug_server()
