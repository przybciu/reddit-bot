import os
import praw

reddit = praw.Reddit(client_secret=os.environ['client_secret'],
                client_id=os.environ['client_id'],
                user_agent=os.environ['user_agent'],
                    username=os.environ['username'],
                    password=os.environ['password'])

subreddit=reddit.subreddit("mptest")
subreddit.submit("title", url="https://www.news.com/")