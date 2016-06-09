""" A simple tool to scrape college football statistics
    for analysis
"""

from server import app

def main():
    """ Test """
    
    app.run('0.0.0.0', debug = True)
    return None


if __name__ == '__main__':
    print('Testing main')
    main()
