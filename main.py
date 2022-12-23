import praw
import os

def makeDirectory(subreddit):
    directory = subreddit
    try:
        os.mkdir(directory)
    except OSError as error:
        print(error)

def storeArticles(subreddit, submission):
    path = subreddit + "/"
    filename = submission.title
    completeName = os.path.join(path, filename+".txt")
    f = open(completeName, "a")
    f.write(submission.selftext)
    f.close()

def searchSub(subreddit, articles):
    reddit = praw.Reddit(
        client_id="T38IvvnBfiZjufqt4rIMiA",
        client_secret="11S6y8H5FFl-A7rBd1oPS5iu03KZmw",
        user_agent="Joe",
    )

    for submission in reddit.subreddit("tifu").hot(limit=articles):
        storeArticles(subreddit, submission)



subreddit = "tifu"
makeDirectory(subreddit)
searchSub(subreddit, 3)
