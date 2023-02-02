

# import the necessary libraries
import json
import requests
from bs4 import BeautifulSoup

# specify the url
url = 'https://www.Netflix.com/'

# query the website and return the html to the variable ‘page’
page = requests.get(url)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

# extract all text from the page and print it out
text = soup.find_all(text=True)
t = text
with open('text.json', 'w') as f:
    json.dump(t, f)
