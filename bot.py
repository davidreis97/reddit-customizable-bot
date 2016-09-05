import praw
import pdb
import re
import os
import time
try:
    from config import *
except:
    print("Please fill in your config.py correctly!")
    exit(1)
from login import *

r = login()

if not os.path.isfile(ANSWERED_COMMENTS_FILE):
    comments_answered = []
else:
    with open(ANSWERED_COMMENTS_FILE,"r") as f:
        comments_answered = f.read()
        comments_answered = comments_answered.split("\n")
        comments_answered.remove("")

while 1:
    if DEBUG:
        print (comments_answered)
    else:
        print ("Running...")
    if POST_ORDER is "hot":
        submissions = r.get_subreddit(SUBREDDIT).get_hot(limit=LIMIT)
    elif POST_ORDER is "new":
        submissions = r.get_subreddit(SUBREDDIT).get_new(limit=LIMIT)
    elif POST_ORDER is "top":
        submissions = r.get_subreddit(SUBREDDIT).get_top(limit=LIMIT)
    elif POST_ORDER is "controversial":
        submissions = r.get_subreddit(SUBREDDIT).get_controversial(limit=LIMIT)
    elif POST_ORDER is "rising":
        submissions = r.get_subreddit(SUBREDDIT).get_rising(limit=LIMIT)
    else:
        print (POST_ORDER, "is an invalid POST_ORDER, check your config.py file")
        exit(1)
    for submission in submissions:
        for comment in submission.comments:
            if KEY_WORD in comment.body:
                com_sub_id = str(submission.id) + str(comment.id)
                if com_sub_id not in comments_answered:
                    comment.reply(COMMENT_PROCESSING(comment.body))
                    comments_answered.append(com_sub_id)
                    with open(ANSWERED_COMMENTS_FILE, "w") as w:
                        for com_id in comments_answered:
                            w.write(com_id + "\n")
                    print ("Answered to comment: ", comment.body, "\nIn thread: ", submission.title)
    time.sleep(TIME_OUT)
