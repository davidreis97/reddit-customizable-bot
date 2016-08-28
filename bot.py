import praw
import pdb
import re
import os
from login-details import * #the login details are on this python file, as strings "USERNAME" and "PASSWORD"

user_agent = ("reverse-text 0.1 // Contact me at /u/SilverTroop")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("bottesting")

if not  os.path.isfile("config_bot.py"):
    print "You must create a file named login-details.py with your username and password."
    exit(1)

r.login(USERNAME, PASSWORD)

if not os.path.isfile("comments_replied_to.txt"):
    posts_replied_to = []
