import praw
import pdb
import re
import os
import time

with open("login-details.txt","r") as l:
    login_details = l.read()
    login_details = login_details.split("\n")

user_agent = ("reverse-text 0.1 // Contact me at /u/SilverTroop or at https://github.com/davidreis97/")

r = praw.Reddit(user_agent = user_agent)

if not  os.path.isfile("login-details.txt"):
    print ("You must create a file named login-details.txt with your username and password.")
    exit(1)

#deprecated
r.login(login_details[0], login_details[1])
#deprecated

if not os.path.isfile("comments_answered.txt"):
    comments_answered = []
else:
    with open("comments_answered.txt","r") as f:
        comments_answered = f.read()
        comments_answered = comments_answered.split("\n")

while 1:
    print (comments_answered)
    submissions = r.get_subreddit('bottesting').get_new(limit=1)
    for submission in submissions:
        for comment in submission.comments:
            if '!reverse' in comment.body:
                com_sub_id = str(submission.id) + str(comment.id)
                if com_sub_id not in comments_answered:
                    response = comment.body.replace("!reverse ","",1)
                    response = response[::-1]
                    comment.reply("###reverse-text-bot\n" + response + "\n___________________\n**I am a bot that reverses text. Come find me at [GitHub](https://github.com/davidreis97/reddit-reverse-bot) or talk to my human creator, /u/SilverTroop**\n")
                    comments_answered.append(com_sub_id)
                    with open("comments_answered.txt", "w") as w:
                        for com_id in comments_answered:
                            w.write(com_id + "\n")
                    print ("Answered to comment", comment, "in thread", submission)
    time.sleep(10)
