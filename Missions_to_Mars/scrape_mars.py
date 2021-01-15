from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# def init_browser():
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

#PART 1 Articles
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    html= browser.html

    soup = bs(html, 'html.parser')
    news_title=soup.find('li', class_="slide").find('div', class_="content_title").text.strip()
    news_p=soup.find('li', class_="slide").find('div', class_="article_teaser_body").text.strip()
    # print(news_title)
    # print(news_p)


# PART 2 Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.find_by_tag('button')[4].click()
    browser.links.find_by_partial_text('Featured Image').click()
    browser.links.find_by_partial_text('Download JPG').click()
    feat_img = browser.find_by_tag('img')['src']


# PART 3 Mars Table
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df=df.rename(columns={0:' ', 1:''})
    df.set_index(' ', inplace=True)
    html_df = df.to_html()
    
    



# PART 4 Hemispheres
    hemispheres = ['Cerberus Hemisphere', 'Schiaparelli Hemisphere', 'Syrtis Major Hemisphere', 'Valles Marineris Hemisphere']
    hemisphere_image_urls=[]

    for x in hemispheres:
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        
        browser.links.find_by_partial_text(f'{x} Enhanced').click()
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('div', class_="downloads").li.a['href']
        img_dict={"title": x, "img_url": img_url}
        hemisphere_image_urls.append(img_dict)
        
    


    #Dictionary to put it all together
    mars_info = {
        "news_title": news_title,
        "news_blurb": news_p,
        "feat_img": feat_img,
        "table": html_df,
        "hemisphere1": hemisphere_image_urls[0],
        "hemisphere2": hemisphere_image_urls[1],
        "hemisphere3": hemisphere_image_urls[2],
        "hemisphere4": hemisphere_image_urls[3]
    }



    browser.quit()


    return mars_info





