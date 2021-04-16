# web-scraping-dashboard

This project uses web scraping and a flask app to present a dashboard of Mars news with recent photos.
The [scraper file](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py) gathers all the information and images from different sites.

The code used to scrape the information is also provided in a [Jupyter Notebook](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb).

The [flask app](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/app.py) uses MongoDB to store and retrieve the scraped information before rendering it to the [html template](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html).

[Screenshots](https://github.com/lmfao415/web-scraping-challenge/tree/main/Missions_to_Mars/Mars%20App%20Screenshots) of the app are included as well.
