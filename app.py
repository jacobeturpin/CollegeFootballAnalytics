""" A simple tool to scrape college football statistics
    for analysis
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


def main():
    """ Test """
    
    app.run('0.0.0.0')
    return None


if __name__ == '__main__':
    print('Testing main')
    main()
