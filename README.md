# reddit-customizable-bot
## Customizable reddit bot that allows the user to create a bot without (much) coding.

### About
Started building by following a guide available [here](http://pythonforengineers.com/build-a-reddit-bot-part-1/), although at this point there is almost no code from there.

You can completely customize the bot's purpose very easily just by changing the config.py file. More settings will be added there as it is my priority to make this bot as customizable as possible, without the end user having to write code at all.

Right now, the example code on config.py answers the reverse of a comment when it's preceded by "!reverse".

### Features
* Uses OAuth2 and safe access storage login
* Allows the user to create and run a fully funcional bot with very little programming knowledge required

### How to Run
* Install the latest stable version of [Python 3](https://www.python.org/)
* Install the [PRAW](https://pypi.python.org/pypi/praw) package (Using the command `pip3 install praw`). Version 4.6.0 is compatible.
* Install the [PyCrypto](https://pypi.python.org/pypi/pycrypto/) package (Using the command `pip3 install pycrypto`). Version 2.6.1 is compatible. This step is optional but recommended, as it will allow you to store your reddit login information on your computer.
* Fill in the blanks on config.py
* Run `python3 bot.py` and follow the instructions to authenticate

### To Do
* [x] Change the authentication method to OAuth2
* [x] Allow the user to (safely) save his login
* [ ] If possible, generate a independent executable file, able to run without the need to `pip install` the dependencies or even Python itself.
* [ ] Give access to more information on the COMMENT_PROCESSING function (post info,parent comment user info, etc)
* [ ] Build an UI to completely remove the necessity of programming by the end user
