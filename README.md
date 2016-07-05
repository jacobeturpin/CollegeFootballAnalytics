# CollegeFootballAnalytics
Simple tool to scrape college football statistics for analysis

# Requirements
* Python 3
* requests
* bs4 (tested using the lxml parser)
* sqlalchemy

# How it Works

The project is divided into three main components:

1. Web scarping component that collects college football statistics
from the web and stores it within a relational database
2. Statistical analysis that leverages historical data to rank
teams/players and predict the outcome of future games
3. Frontend to display data visualizations and summarized portions of 
item #2 on the web

The three components are intended to be run concurrently as three 
separate processes using the runserver.py file. 

# Running Tests
Projects tests may be run using the runtests.py file

```bash
python runtests.py
```