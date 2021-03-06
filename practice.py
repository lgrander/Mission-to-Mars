from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'

browser.visit(url)

# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')

# Scrape the Title
title = html_soup.find('h2').text
title

# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)

url = 'http://quotes.toscrape.com/'
browser.visit(url)    

for x in range(1, 6):
   html = browser.html
   quote_soup = soup(html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next').click()