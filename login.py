import praw
import webbrowser
try:
    from config import *
except:
    print("Please fill in your config.py correctly!")
    exit(1)

def login():
    r = praw.Reddit(user_agent = USER_AGENT)
    r.set_oauth_app_info(client_id='Qhe0Btx7BlYiXw',client_secret='',redirect_uri='http://redditcustomizablebot.comli.com/oauthcode.html')
    url = r.get_authorize_url('rcbunique', 'submit read', True)
    webbrowser.open(url)
    oauthcode = input('Paste the key from the website: ')
    access_information = r.get_access_information(oauthcode)
    return r
