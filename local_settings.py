#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'CONSUMER_KEY'
MY_CONSUMER_SECRET = 'CONSUMER_SECRET'
MY_ACCESS_TOKEN_KEY = 'ACCESS_TOKEY_KEY'
MY_ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

SOURCE_ACCOUNTS = ["twnsndco"]
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "twnsndco" #The name of the account you're tweeting to.
