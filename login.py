import praw
import webbrowser
import os

def login():
    #Allows me to use my own private config file without changing any code. You should only use config.py.
    if os.path.isfile('config_private.py'):
        from config_private import USER_AGENT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
    else:
        try:
            from config import USER_AGENT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
        except:
            print("Please fill in your config.py correctly!")
            exit(1)
    
    r = praw.Reddit(user_agent = USER_AGENT)
    r.set_oauth_app_info(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)
    url = r.get_authorize_url('rcbunique', 'submit read', True)
    webbrowser.open(url)
    oauthcode = input('Paste the key from the website: ')
    access_information = r.get_access_information(oauthcode)
    return r
