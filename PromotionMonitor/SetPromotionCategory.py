__author__ = 'jessie'

from alchemyapi import AlchemyAPI
import json


class SetCategory():
    def __init__(self, text):
        print text
        alchemyapi = AlchemyAPI()

        response = alchemyapi.concepts('text', text)

        if response['status'] == 'OK':
            print('## Response Object ##')
            print(json.dumps(response, indent=4))

            print('')
            print('## Concepts ##')
            for concept in response['concepts']:
                print('text: ', concept['text'])
                print('relevance: ', concept['relevance'])
                print('')
        else:
            print('Error in text categorization call: ', response['statusInfo'])



SetCategory('Bob breaks my fancy iphone and I have to send it to Apple store to repair.')



