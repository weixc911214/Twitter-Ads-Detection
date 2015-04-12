## How AccountManager works

### How to run the code

To run the code, you should first install some packages using **pip**. Here are some packages you need to install:

```
pip install tweepy
pip install python-twitter
```

### Set up the config files

For now, there are two import config files in the configs folder: **accounts_config** and **application_config**.

#### 1. application_config

In the application_config file, there are only 2 lines, they are the consumerkey and the consumersecret of your Twitter Application. The format is shown as following:

```
consumer_key=anbpwuMUw7nIlo5SXAxCU803j
consumer_secret=u2yVCFbi7os8dFrSUwmk4zzGRuyLMWkghHw1HcSiIMvSqHPp2p
```

#### 2. accounts_config

In the accounts config file, each line is the config of one Twitter account, the format is shown as following:

> username : password : default_keyword : access-token(optional) : access secret(optional)

Your can insert each user into the accounts config like:

> 274558119@qq.com:wxc16888:NBA:3154095670-KzH1kiSRcMnObQhIkTcxLzbL8HnTSYEruOGYRhW:vMM6yOJLvVUpLxRf6W0qW2ImIS2tA1Ky9QbMiIA63r7VZ

or like:

> 274558119@qq.com:wxc16888:NBA

if the new created twitter account has not got access token to our Twitter application in the application config file, you could run

> get_access_token.py

to get the access token for the user and store the information in the account_config.

PS: for the default keyword, the user will post twiteer with this keyword if you don't specify any other keyword in the **post(user, keyword)** function in the AccountManager.

