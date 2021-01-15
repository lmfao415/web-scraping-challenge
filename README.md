# web-scraping-challenge

This project combines different scraped information about Mars along with images into one page using flask.

The [scraper file](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py) gathers all the information and images from different sites.

The [flask app](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/app.py) uses MongoDB to store and retrieve the scraped information before rendering it to the [html template](https://github.com/lmfao415/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html)
