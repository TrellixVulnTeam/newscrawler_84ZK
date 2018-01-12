import sys
from datetime import datetime
from urllib.request import Request, urlopen
from pymongo import MongoClient
from bs4 import BeautifulSoup

# Number of pages to crawl (By default 3)
n = 3
if len(sys.argv) == 2:
    n = int(sys.argv[1])

# First page to open
next_page = "https://www.reddit.com/r/Python/"

# To avoid the error: "urllib.error.HTTPError: HTTP Error 429: Too Many Requests"
hdr = {'User-Agent': 'new user-agent'}

# Connect to database with default configuration
client = MongoClient()
db = client.newscrawler
db.users.create_index("username", unique=True)

while n > 0:
    # Parse the page to a Python object
    req = Request(next_page, headers=hdr)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    # Get all the news
    entries = soup.findAll("div", {"class": "link"})
    for entry in entries:
        # Gather the information that we need
        submission = {}
        submission['punctuation'] = entry["data-score"]
        submitter = entry["data-author"]
        submission['number_comments'] = entry["data-comments-count"]
        submission['url'] = entry["data-url"]
        if entry["data-domain"] == "self.Python":  # Is a discussion
            submission['url'] = "https://www.reddit.com" + submission['url']  # In this case the url is relative
            submission['is_discussion'] = True
        else:
            submission['is_discussion'] = False
        submission['title'] = entry.find("a", {"class": "title"}).getText()
        submission['creation_date'] = entry.find("time")["datetime"]

        # Insert submission
        id_submission = db.submissions.insert_one(submission).inserted_id
        # Insert user
        db.users.update_one({'username': submitter}, {'$push': {'submissions': id_submission}}, upsert=True)

    next_page = soup.find("span", {"class": "nextprev"}).find("a")["href"]
    n = n - 1
