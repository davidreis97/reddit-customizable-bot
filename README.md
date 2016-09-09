# reddit-customizable-bot
## Customizable reddit bot that allows the user to create a bot without (much) coding.

### About
Started building by following a guide available [here](http://pythonforengineers.com/build-a-reddit-bot-part-1/), although at this point there is almost no code from there.

You can completely change the bot's purpose very easily just by changing the config.py file. More settings will be added there as it is my priority to make this bot as customizable as possible, without the end user having to write code at all.

Right now, the example code on config.py answers the reverse of a comment when it's preceded by "!reverse".

### How to Run
* Install the latest version of python 3 and install the "praw" package (Using the command `pip3 install praw`)
* Fill in the blanks on config.py
* Run `python3 bot.py` and follow the instructions to authenticate

### To Do
* Add more settings to config.py (Continuous task)
* [x] Change the authentication method to OAuth2
* [ ] Build an UI to completely remove the necessity of programming by the end user
