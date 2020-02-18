# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:35:16 2020

@author: vidhy
"""
# Load the tweepy Library
import tweepy
import json
from googlesearch import search

#  Twitter Api Key 
#Twitter Devloper credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
# Testing Connection
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
print(api)


api.update_status
#using canada geo code.Can use your own country code
CANADA_WOE_ID=23424775
#searching the trends in canada
canada_trends = api.trends_place(CANADA_WOE_ID)

canada_trends= json.loads(json.dumps(canada_trends, indent=1))
#dictonary to store the trend and related google search url
canada_trends_with_GoogleLink={}
c=1
for trend in canada_trends[0]["trends"]:
    #using googlesearch library to search trending topic on internet.
    for url in search(trend['name'].strip("#"), tld="com", num=10, stop=1, pause=2):
        if c<11:
            #Storing the url into a dictionary using key as topic and value as Url
            canada_trends_with_GoogleLink[trend['name']]=url
            c=c+1
        else:
            break
#print the trend name with url
print("TOPIC\t\t\t\t\t\tURL")
for key in canada_trends_with_GoogleLink:
    print(key+"\t:\t"+canada_trends_with_GoogleLink.get(key))
