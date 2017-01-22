import praw
import webbrowser
import os
try:
    from Crypto.Cipher import AES
    AccessStorage = True
except:
    print("WARNING: PyCrypto wasn't found on this machine. Read the README for more info.")
    AccessStorage = False
import getpass
import base64
import traceback
import sys
#Allows me to use my own private config file without changing any code. You should only use config.py.
if os.path.isfile('config_private.py'):
    from config_private import *
    print("Using private configuration file.")
else:
    try:
        from config import *
    except:
        print("Please fill in your config.py correctly!")
        exit(1)

def login():
    finished = False
    while (finished == False):
        try:
            userinput = "N"
            if AccessStorage and os.path.isfile('.authkey'):
                userinput = input('Do you wish to log in to your saved account? (Y/N): ')
            if userinput == "Y":
                pswd = getpass.getpass('Password: ').rjust(32,'0')
                with open('.authkey',"rb") as f:
                    pswdfile = f.read()
                    pswdfile = pswdfile.split("\n".encode('ascii')) 
                iv = pswdfile[1]               
                cipher = AES.new(pswd,AES.MODE_CFB,iv)
                file_refresh_token = cipher.decrypt(base64.b64decode(pswdfile[0]))
                if DEBUG:
                    print ("Refresh token decrypted: ",file_refresh_token)
                print("Attempting to connect to reddit...")
                r = praw.Reddit(user_agent = USER_AGENT, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, refresh_token= file_refresh_token)
                print ("Success! You're now logged in as ", r.user.me(),".")
            else:
                r = praw.Reddit(user_agent = USER_AGENT, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)
                scopes = ['read','submit','identity'] + EXTRA_SCOPE
                if DEBUG:
                    print ("Scopes: ", scopes)
                url = r.auth.url(scopes, '-', 'permanent')
                webbrowser.open(url)
                oauthcode = input('Paste the key from the website: ')
                print("Attempting to connect to reddit...")
                refresh_token = r.auth.authorize(oauthcode)
                print ("Success! You're now logged in as ", r.user.me(),".")
                if AccessStorage: 
                    userinput = input('Do you wish to save your credentials on this computer? (Y/N): ')
                if userinput == "Y":
                    pswd = getpass.getpass('Please enter a password. You will be required to enter this password to login to your reddit account: ').rjust(32,'0')
                    iv = os.urandom(16)
                    cipher = AES.new(pswd,AES.MODE_CFB,iv)
                    encoded_refresh_token = base64.b64encode(cipher.encrypt(refresh_token))
                    with open('.authkey',"wb") as f:
                        f.write(encoded_refresh_token + "\n".encode('ascii'))
                        f.write(iv)
            finished = True
        except:
            if DEBUG:
                traceback.print_exc()
            exit = input('An error occurred, do you wish to try again? (Y/N): ')
            if exit == "N":
                sys.exit()
    return r
