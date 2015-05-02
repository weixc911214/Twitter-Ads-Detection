__author__ = 'wei'
import pymysql as sql

class TwitterImporter:
    def __init__(self):
        self.db = sql.connect(host='cloud.comtnuycjpkv.us-west-2.rds.amazonaws.com', user='weixc1234', passwd='wxc16888', db='Twitter', cursorclass=sql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def update_promotion(self, username, tweet, promoted_source, img_url):
        sql = "insert into promotions(username, content, promoted_source, img_url) values (\"%s\",\"%s\",\"%s\",\"%s\")" \
        % (username, tweet, promoted_source, img_url)
        self.cursor.execute(sql)
        self.db.commit()
