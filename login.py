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
if os.path.isfile('config_private.py'):
    from config_private import *
else:
    try:
        from config import *
    except:
        print("Please fill in your config.py correctly!")
        exit(1)

def login():
    #Allows me to use my own private config file without changing any code. You should only use config.py.

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
                print("Success!")
            else:
                r = praw.Reddit(user_agent = USER_AGENT, client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)
                url = r.auth.url(['read','submit','identity'] + EXTRA_SCOPE, '-', 'permanent')
                webbrowser.open(url)
                oauthcode = input('Paste the key from the website: ')
                print("Attempting to connect to reddit...")
                print("Success!")
                if AccessStorage: 
                    userinput = input('Do you wish to save your credentials on this computer? (Y/N): ')
                if userinput == "Y":
                    pswd = getpass.getpass('Please enter a password. You will be required to enter this password to login to your reddit account: ').rjust(32,'0')
                    iv = os.urandom(16)
                    cipher = AES.new(pswd,AES.MODE_CFB,iv)
                    encoded_refresh_token = base64.b64encode(cipher.encrypt(r.auth.authorize(oauthcode)))
                    with open('.authkey',"wb") as f:
                        f.write(encoded_refresh_token + "\n".encode('ascii'))
                        f.write(iv)
            finished = True
            print ("You're now logged in as ", r.user.me(),".")
        except:
            if DEBUG:
                traceback.print_exc()
            exit = input('An error occurred, do you wish to try again? (Y/N): ')
            if exit == "N":
                sys.exit()
    return r
