import praw
import webbrowser
import os
try:
    from Crypto.Cipherr import AES
    AccessStorage = True
except:
    AccessStorage = False
import getpass
import base64
import traceback
import sys

def login():
    #Allows me to use my own private config file without changing any code. You should only use config.py.
    if os.path.isfile('config_private.py'):
        from config_private import USER_AGENT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, DEBUG
    else:
        try:
            from config import USER_AGENT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, DEBUG
        except:
            print("Please fill in your config.py correctly!")
            exit(1)
    
    r = praw.Reddit(user_agent = USER_AGENT)
    r.set_oauth_app_info(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI)
    finished = False
    while (finished == False):
        try:
            userinput = "N"
            if AccessStorage and os.path.isfile('.authkey'):
                userinput = input('Do you wish to log in to your saved account? (Y/N): ')
            if os.path.isfile('.authkey') and userinput == "Y":
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
                r.refresh_access_information(file_refresh_token)
                print("Success!")
            else:
                url = r.get_authorize_url('rcbunique', 'submit read', True)
                webbrowser.open(url)
                oauthcode = input('Paste the key from the website: ')
                print("Attempting to connect to reddit...")
                access_information = r.get_access_information(oauthcode)
                print("Success!")
                if AccessStorage: 
                    userinput = input('Do you wish to save your credentials on this computer? (Y/N): ')
                if userinput == "Y":
                    pswd = getpass.getpass('Please enter a password. You will be required to enter this password to login to your reddit account: ').rjust(32,'0')
                    iv = os.urandom(16)
                    cipher = AES.new(pswd,AES.MODE_CFB,iv)
                    encoded_refresh_token = base64.b64encode(cipher.encrypt(access_information['refresh_token']))
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
