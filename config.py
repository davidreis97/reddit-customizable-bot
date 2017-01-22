#Use this file to edit the bot behaviour.

#Your user agent
USER_AGENT =

#File name in which you wish to keep record of the comments the bot already answered
ANSWERED_COMMENTS_FILE = "comments_answered.txt"

#SUBREDDIT on which you wish to search for posts (without the "/r")
SUBREDDIT =

#How many posts do you wish to search for
LIMIT =

#List of posts to search in (hot,new,rising,top,controversial)
POST_ORDER =

#Key word that triggers the bot to answer a comment
KEY_WORD = "!reverse"

#Least amount of time (in seconds) that the bot will wait after each search for comments (0 is not advised)
TIME_OUT =

#Function that receives the original comment and returns the answer that the bot will post
def COMMENT_PROCESSING(comment,submission):
    #EXAMPLE CODE
    response = comment.body.replace(KEY_WORD,"",1)
    response = response[::-1]
    return("###reverse-text-bot\n" + response + "\n___________________\n**I am a bot that reverses text. Come find me at [GitHub](https://github.com/davidreis97/reddit-reverse-bot) or talk to my human creator, /u/SilverTroop**\n")

#----------------------------------------------------------------------
#ADVANCED VARIABLES (don't change unless you know what you're doing)
#----------------------------------------------------------------------

#OPTIONAL - If you wish to have access to any other scope on reddit other than 'read', 'submit' and 'identity' insert them here in the form ['scope1','scope2',...] or leave [] if you do not wish to add any other scope.
#Documentation for all reddit API scopes available at https://www.reddit.com/dev/api/oauth/
#Any time you wish to change this you cannot login with the saved data on your computer.
EXTRA_SCOPE = []

DEBUG = 0

CLIENT_ID = 'Qhe0Btx7BlYiXw'

CLIENT_SECRET = 'NONE'

REDIRECT_URI = 'http://redditcustomizablebot.comli.com/oauthcode.html'
