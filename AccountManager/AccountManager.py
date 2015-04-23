__author__ = 'wei'
import tweepy
from random import randint
from tweepy.error import TweepError
from AccountOauth import get_access_token
'''
AccountManger: Manage the behaviors of user accounts

The main functions of this class are:

    1. Randomly choose an account from our account sets
    2. select the rule, specified or randomly for the chosen account
    3. mock user behavior with selected rules

'''


class AccountManager():
    def __init__(self, accounts_config="configs/accounts_config", application_config="configs/application_config",
                 rule_config="configs/rule_config", idle_time=5):

        # load configs
        self.accounts_config = accounts_config
        self.consumer_key, self.consumer_secret = self._init_application(application_config)
        self.accounts_list = self._load_accounts(self.accounts_config)
        self.rule_sets = self._load_rules(rule_config)

        # the idle time of mocking user behaviors
        self.idle_time = idle_time
        self.api = None

    def print_info(self):
        print "The information of AccountManager:"
        print "accounts_list: " + str(self.accounts_list)
        print "rule_sets: " + str(self.rule_sets)
        print "idle time: " + str(self.idle_time)

    '''
    load accounts information
    '''

    def _load_accounts(self, accounts_config):
        accounts_list = list()
        with open(accounts_config) as account_file:
            accounts = account_file.readlines()
            for account in accounts:
                account = account.split(":")
                #print account
                username = account[0]
                password = account[1]
                default_keyword = account[2]

                try:
                    access_token = account[3]
                    access_token_secret = account[4]
                except StandardError:
                    print "this account %s has not get the access token, please use get_access_token.py" % username
                    break
                    # access_token, access_token_secret = get_access_token(self.consumer_key, self.consumer_secret)
                account_info = {"username": username,
                                "password": password,
                                "keyword": default_keyword,
                                "access_token": access_token,
                                "access_token_secret": access_token_secret}

                accounts_list.append(account_info)

        return accounts_list

    '''
    load application configs
    '''
    @staticmethod
    def _init_application(application_config):
        with open(application_config) as application_config:
            contents = [line.strip().split("=") for line in application_config.readlines()]

        consumer_key = contents[0][1]
        consumer_secret = contents[1][1]

        return consumer_key, consumer_secret

    '''
    update the accounts list from accounts file
    '''
    def _update_accounts(self):
        self.accounts_list = self._load_accounts(self.account_config)

    '''
    load defined user behavior rules
    '''
    @staticmethod
    def _load_rules(rule_config):
        return "No Rules"

    '''
    TODO: test if the api has been successfully accessed
    '''
    def test_api(self):
        try:
            self.get_twitter_by_keyword("NBA")
            print "Call API successfully!"
        except ImportError:
            print "Something wrong in when calling API!"

    '''
    call api to get one twitter by keyword
    '''
    def get_twitter_by_keyword(self, keyword):
        text = ""
        try:
            results = self.api.search(keyword)
            random = randint(0, len(results) - 1)
            twitter = results[random]
            text = twitter.text
        except:
            text = keyword
        return text

    # TODO: mock user behavior with chosen user account and twitter
    def post(self, user, keyword=""):
        if len(keyword) == 0:
            keyword = user["keyword"]
        text = self.get_twitter_by_keyword(keyword)

        try:

            self.api.update_status(status=text)
            print "User: %s" % user["username"]
            print "Keyword: %s" % keyword
            print "Post: %s" % text


        except TweepError:
            print "Headers indicate a formencoded body but body was not decodable."

    '''
    get one account from accounts_list
    '''
    def get_random_user(self):
        account_number = len(self.accounts_list)
        # print account_number
        index = randint(0, account_number - 1)
        # print index
        user_info = self.accounts_list[index]
        consumer_key = self.consumer_key
        consumer_secret = self.consumer_secret
        access_token = user_info["access_token"]
        access_token_secret = user_info["access_token_secret"]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        return user_info

    # TODO: run the Account Manager
    def run(self):
        test_user = self.get_random_user()
        self.post(user=test_user)

    # getter and setter
    def get_idle_time(self):
        return self.idle_time

    def set_idle_time(self, idle_time):
        self.idle_time = idle_time


if __name__ == "__main__":

    am = AccountManager()
    count = 0
    import time
    while count < 60:
        try:
            user = am.get_random_user()
            am.post(user)
        except TweepError:
            print "err"
        count = count + 1
        time.sleep(30)

