__author__ = 'jessie'

import MySQLdb
from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()

db = MySQLdb.connect('cloud.comtnuycjpkv.us-west-2.rds.amazonaws.com', 'weixc1234', 'wxc16888', 'Twitter')

cursor = db.cursor()

cursor.execute('SELECT id, content FROM promotions')

rows = cursor.fetchall()

for row in rows:
    response = alchemyapi.keywords('text', row[1], {'sentiment': 1})

    if response['status'] == 'OK':
        key = []
        rel = []
        count = 0
        for keyword in response['keywords']:
            key.append(keyword['text'].encode('utf-8'))
            rel.append(keyword['relevance'])
            count = count + 1


        # Prepare SQL query to INSERT a record into the database.
        try:
           # Execute the SQL command
           cursor.execute("""UPDATE Twitter.promotions SET keyword1 = %s, relevance1 = %s,keyword2 = %s, relevance2 = %s,keyword3 = %s, relevance3 = %s WHERE id = %s""",(key[0],rel[0],key[1],rel[1],key[2],rel[2],row[0]))
           print 'ok'
           # Commit your changes in the database
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    else:
        print('Error in : ', response['statusInfo'])


# disconnect from server
db.close()






