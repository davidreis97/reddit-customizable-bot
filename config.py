#Use this file to edit the bot behaviour.

#Your user agent
USER_AGENT =

#File name in which you wish to keep record of the comments the bot already answered
ANSWERED_COMMENTS_FILE = "comments_answered.txt"

#SUBREDDIT on which you wish to search for posts
SUBREDDIT =

#How many posts do you wish to search for
LIMIT =

#List of posts to search in (hot,new,rising,top,controversial)
POST_ORDER =

#Key word that triggers the bot to answer a comment
KEY_WORD = "!reverse"

#Time (in seconds) that the bot will wait after each search for comments (0 is not advised)
TIME_OUT =

#Function that receives the original comment and returns the answer that the bot will post
def COMMENT_PROCESSING(comment):
    #EXAMPLE CODE
    response = comment.replace(KEY_WORD,"",1)
    response = response[::-1]
    return("###reverse-text-bot\n" + response + "\n___________________\n**I am a bot that reverses text. Come find me at [GitHub](https://github.com/davidreis97/reddit-reverse-bot) or talk to my human creator, /u/SilverTroop**\n")

#---------------------
#DEVELOPMENT VARIABLES
#---------------------

DEBUG = 0
