import pdb
import re
import os
import time
import sys
try:
    import praw
except:
    print("Please read the README and install all the required dependencies. (PRAW is missing)")
    sys.exit()

#Allows me to use my own private config file without changing any code. You should only use config.py.
if os.path.isfile('config_private.py'):
    from config_private import *
else:
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

while 1:
    if DEBUG:
        print (comments_answered)
    else:
        print ("Running...")
    if POST_ORDER is "hot":
        submissions = r.subreddit(SUBREDDIT).hot(limit=LIMIT)
    elif POST_ORDER is "new":
        submissions = r.subreddit(SUBREDDIT).new(limit=LIMIT)
    elif POST_ORDER is "top":
        submissions = r.subreddit(SUBREDDIT).top(limit=LIMIT)
    elif POST_ORDER is "controversial":
        submissions = r.subreddit(SUBREDDIT).controversial(limit=LIMIT)
    elif POST_ORDER is "rising":
        submissions = r.subreddit(SUBREDDIT).rising(limit=LIMIT)
    else:
        print (POST_ORDER, "is an invalid POST_ORDER, check your config.py file")
        exit(1)
    for submission in submissions:
        for comment in submission.comments:
            if KEY_WORD in comment.body:
                com_sub_id = str(submission.id) + str(comment.id)
                if com_sub_id not in comments_answered:
                    comment.reply(COMMENT_PROCESSING(comment,submission))
                    comments_answered.append(com_sub_id)
                    with open(ANSWERED_COMMENTS_FILE, "w") as w:
                        for com_id in comments_answered:
                            w.write(com_id + "\n")
                    print ("Answered to comment: ", comment.body, "\nIn thread: ", submission.title)
    time.sleep(TIME_OUT)
    
