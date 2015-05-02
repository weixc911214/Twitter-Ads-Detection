__author__ = 'wei'
import bs4
from selenium import webdriver
import pymysql as sql

class TwitterImporter:
    def __init__(self):
        self.db = sql.connect(host='cloud.comtnuycjpkv.us-west-2.rds.amazonaws.com', user='weixc1234', passwd='wxc16888', db='Twitter', cursorclass=sql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def update_promotion(self, username, tweet, promoted_source, img_url):
        sql = "insert into promotions(username, content, promoted_source, img_url) values (\"%s\",\"%s\",\"%s\",\"%s\")" \
        % (username, tweet, promoted_source, img_url)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            pass
    def update_tweet(self, username, tweet):
        sql = "insert into twitters(username, content) values(\"%s\", \"%s\")" %(username, tweet)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            pass

def handle_promotion(username, password):

    driver = webdriver.Firefox()

    # load Twitter login page
    driver.get("https://twitter.com/login")

    # find the username and password element
    username_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
    password_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")

    # type in username and password
    username_element.send_keys(username)
    password_element.send_keys(password)

    # click Sign In and we should be logged in
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button').click()

    # the following javascript scrolls down the entire page body.  Since Twitter
    # uses "inifinite scrolling", more content will be added to the bottom of the
    # DOM as you scroll... since it is in the loop, it will scroll down up to 100
    # times.
    for _ in range(30):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # print all of the page source that was loaded
    f = open('twitter.html', 'w')
    print "hello"
    f.write(driver.page_source.encode("utf-8"))
    f.close()

    # quit and close browser
    driver.quit()
    pe = PromotionExtractor("twitter.html")
    result = pe.soup.find_all(attrs={"data-item-type": "tweet"})
    nick_name = pe.soup.find(attrs={"class":"u-textInheritColor"}).text
    for r in result:
        promotion_contents = r.find_all(attrs={"class": "js-promoted-badge"})
        if len(promotion_contents) > 0:
            content = r.find_all(attrs={"class": "content"})
            content = content[0]

            # get promotion tweets
            text = content.find(attrs={"class": "tweet-text"}).text

            # get promotion creator
            context = content.find_all(attrs={"class": "context"})
            promoted_source = ""
            if len(context) > 0:
                promoted_source = context[0].find(attrs={"class": "js-promoted-badge"}).text

            creator = content.find_all(attrs={"class": "promoted-account-in-timeline-name"})
            if len(creator) > 0:
                promoted_source = creator[0].find(attrs={"class": "fullname"}).text


            # get the promotion image, if they have
            media = content.find_all(attrs={"class": "js-media-container"})
            img_url = ""
            if len(media) == 2:
                img_contents = media[0].find_all(attrs={"alt": "Embedded image permalink"})
                if len(img_contents) > 0:
                    img_url = img_contents[0]['src']


            text =  text.encode("utf8")
            promoted_source = promoted_source.encode("utf8")


            source = ""
            for word in promoted_source.split(" ")[1:-1]:
                source = source + word + " "
            promoted_source = source.strip()

            pe.importer.update_promotion(username, text, promoted_source, img_url)
            #
            # print "-----"
            # print "Tweet: " + text
            # print "Promotion Source: " + promoted_source
            # print "promotion image: " + img_url

def handle_tweets(username, password):
    driver = webdriver.Firefox()

    # load Twitter login page
    driver.get("https://twitter.com/login")

    # find the username and password element
    username_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
    password_element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")

    # type in username and password
    username_element.send_keys(username)
    password_element.send_keys(password)

    # click Sign In and we should be logged in
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button').click()

    driver.get("https://twitter.com/AllenAtl")

    for _ in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # print all of the page source that was loaded
    f = open('tweets.html', 'w')
    print "hello"
    f.write(driver.page_source.encode("utf-8"))
    f.close()

    # quit and close browser
    driver.quit()

    pe = PromotionExtractor("tweets.html")
    result = pe.soup.find_all(attrs={"data-item-type": "tweet"})
    nick_name = pe.soup.find(attrs={"class":"u-textInheritColor"}).text


    for r in result:

        content = r.find(attrs={"class": "ProfileTweet"})

        if content is not None:
            header = content.find(attrs={"class": "ProfileTweet-header"})
            #print header
            try:
                account_name = header.find(attrs={"class": "ProfileTweet-fullname"}).text
                text = content.find(attrs={"class": "ProfileTweet-text"}).text
                text = text.encode("utf8")
                pe.importer.update_tweet(username, text)
            except:
                pass



class PromotionExtractor():
    def __init__(self, html):
        input_file = open(html)
        self.soup = bs4.BeautifulSoup(input_file)
        self.importer = TwitterImporter()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
       username =  sys.argv[1]
       password = sys.argv[2]

       handle_promotion(username, password)
       handle_tweets(username, password)


        # else:











