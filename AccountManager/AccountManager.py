__author__ = 'wei'
import tweepy
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
        self.api = self._init_application(application_config)
        self.accounts_list = self._load_accounts(accounts_config)
        self.rule_sets = self._load_rules(rule_config)

        # the idle time of mocking user behaviors
        self.idle_time = idle_time

    def print_info(self):
        print "The information of AccountManager:"
        print "accounts_list: " + str(self.accounts_list)
        print "rule_sets: " + str(self.rule_sets)
        print "idle time: " + str(self.idle_time)

    '''
    load accounts information
    '''
    @staticmethod
    def _load_accounts(accounts_config):
        accounts_list = list()
        with open(accounts_config) as account_file:
            accounts = account_file.readlines()
            for account in accounts:
                account = account.split(":")
                username = account[0]
                password = account[1]
                default_keyword = account[2]
                account_info = {"username": username, "password": password, "keyword": default_keyword}
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
        access_token = contents[2][1]
        access_token_secret = contents[3][1]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        return api

    '''
    test if the api has been successfully accessed
    '''
    def test_api(self):
        pass

    '''
    load defined user behavior rules
    '''
    @staticmethod
    def _load_rules(rule_config):
        return "No Rules"

    # TODO: call api to get one twitter by keyword
    def get_twitter_by_keyword(self, keyword):
        pass

    # TODO: mock user behavior with chosen user account and twitter
    def post(self, user, twitter):
        pass

    # TODO: get one account from accounts_list
    def get_random_user(self):
        pass

    # TODO: run the Account Manager
    def run(self):
        pass

    # getter and setter
    def get_idle_time(self):
        return self.idle_time

    def set_idle_time(self, idle_time):
        self.idle_time = idle_time


if __name__ == "__main__":

    am = AccountManager()
    am.print_info()