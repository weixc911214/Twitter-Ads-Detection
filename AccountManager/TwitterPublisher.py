# -*- coding: utf-8 -*-
__author__ = 'wei'

import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup, Tag, NavigableString


class TwitterPublisher():

    def __init__(self):
        self.login_url = "https://mobile.twitter.com/session/new"
        self.redirect_url = "https://mobile.twitter.com/compose/tweet"
        self.session = requests.session()

    def log_in(self, username, password):
        response = self.session.get(self.login_url).text
        soup = BeautifulSoup(response)
        # get the hidden authenticity_token
        authenticity_token = soup.find(attrs={"name": "authenticity_token"})["value"]
        username = username
        password = password
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : '******'}
        data = {
            "authenticity_token": authenticity_token,
            "session[username_or_email]": "wxc16888",
            "session[password]": password,
            "remember_me": "1",
            "wfa": "1",
            "commit": " Log in "
        }
        print "log in"
        keep_request = 1
        while keep_request == 1:
            try:
                r = self.session.post(self.login_url, data, headers)
                print r

                keep_request = 0

            except StandardError:
                print "request again"

            print "login successfully!"

    def get_url_contents(self, url):
        keep_request = 1
        contents = ""
        while keep_request == 1:
            try:
                response = self.session.get(url)
                contents = response.text
                keep_request = 0
            except StandardError:
                print "request %s again" % url

        return contents

    def post(self):
        pass

if __name__ == "__main__":
    twitter = TwitterPublisher()
    twitter.log_in("274558119@qq.com", "wxc1688")