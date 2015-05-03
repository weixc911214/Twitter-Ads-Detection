__author__ = 'jessie'

from alchemyapi import AlchemyAPI
import json


class GetKeywords():
    def __init__(self, text):
        alchemyapi = AlchemyAPI()

        response = alchemyapi.keywords('text', text, {'sentiment': 1})

        if response['status'] == 'OK':
            for keyword in response['keywords']:
                print('text: ', keyword['text'].encode('utf-8'))
                print('relevance: ', keyword['relevance'])
                print('')
        else:
            print('Error in : ', response['statusInfo'])



GetKeywords('Bob breaks my fancy iphone and I have to send it to Apple store to repair.')



