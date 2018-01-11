import urllib.request
from time import sleep
from pymongo import MongoClient
from bs4 import BeautifulSoup

# Connect to default settings
client = MongoClient()
# Get the database
db = client.newscrawlerDB

# Connect to python subreddit
page = urllib.request.urlopen("https://www.reddit.com/r/Python/").read()
# Parse html to Python object
soup = BeautifulSoup(page, "html.parser")
# Get only the news
entries = soup.findAll("div", {"class": "entry unvoted"})
for entry in entries:
    # Get params of entrys
    title = entry.find("p", {"class": "title"}).find("a").getText()
    print(title)
