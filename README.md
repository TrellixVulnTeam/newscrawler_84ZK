# News Crawler
News Crawler is composed of a script that gather information of every submission in [python subreddit](https://www.reddit.com/r/Python/) and a Rest API that give some statistics of this information.

### Assuptions
* The API readings have to be more efficient than the writings of the script in the database.
* The script only runs one time and the database is empty, so I don't have to check if the news exists in the database or not.
* For the design of the database I have only taken into account the API calls that I could do saving only the submissions and submitters. 

### Decisions
I have experience with Django and Mongo, but not in the same project. So I decided to develop this API with Mongo to gain experience devoloping with this two technologies together.

For the API I decided to use the [Django-rest-framework](http://www.django-rest-framework.org/) because is the most common.

For the tests I decided to run in a diferent database.

For reason of time, because I am writting my degree thesis at the moment, I decided to save and give statistics only of the news and submitters, but not of the comments.


### Design
The design is not complex, it is composed of a script that save the news and submitters in the database and an API that give the statistics.

The design of the database has changed. At the begining I tried to make one collection with all the submitions and its submitters embedded. With this design, the inserts are fast (because I could use the insertMany function), but it creates a lot of repeated users, the readings are less efficient and the mapReduce function is needed to know the top submitters. 

So, taking into account that the API calls return information only related to submissions or users, except all the submissions of a user that is needed a join (not efficient in mongo), I decided to make two collections, Submissions and Users. The inserts are less efficient because I have to check if every user exists or not and I can't use the insertMany function, but now the readings are faster and simplier.

I had to create a unique index in the username field of the users collections to check if the user exists or not.

## Getting started

### Prerequisites
Before download the project, check if you have installed the Python 3.6.4 and MongoDB. If not, go to the following links and download it.
- [Python 3.6.4](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/download-center#atlas)

### Installing
First of all download or clone the project.

```
git clone https://github.com/victorggep/newscrawler.git
```

If you want, you can install a virtual environment.

Install the project dependencies:

```
pip install -r requirements.txt
```

Start the MongoDB. 

If you use the default configuration skip this step. If not, go to newscrawler/settings and change the following configuration to yours. You can add user, password, port, whatever you need.
```
MONGODB_DATABASES = {
    "default": {
        "name": "newscrawler",
        "host": "localhost",
    },

    "test": {
        "name": "test",
        "host": "localhost",
    }
}

mongoengine.connect(
    db=MONGODB_DATABASES[db]['name'],
    host=MONGODB_DATABASES[db]['host']
)
```
You have to change in crawler.py too:
```
client = MongoClient()
```

## Running the tests
Run the tests to check if the connection to the Mongo is well configurated and the API works well.

```
./manage.py test
```
## Deployment
First of all, run the script that save all the information to the database.

You can run it crawling only the first 3 pages of the subreddit:
```
python crawler.py
```
Or you can run it crawling the N pages that you want:
```
python crawler.py N
```

After it, run the API:
```
python manage.py runserver
```

## API Urls

- /api/submissions/{id}/
- /api/submissions/top/points/any/
- /api/submissions/top/points/discussions/
- /api/submissions/top/points/articles/
- /api/submissions/top/discussed/any/
- /api/submissions/top/discussed/discussions/
- /api/submissions/top/discussed/articles/
- /api/users/{id}/ 
- /api/users/{id}/posts/
- /api/users/top/submitters/


## Authors

* **Víctor González Garrido**

