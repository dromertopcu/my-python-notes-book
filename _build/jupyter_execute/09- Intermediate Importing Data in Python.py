#!/usr/bin/env python
# coding: utf-8

# ## Intermediate Importing Data in Python

# ### Importing flat files from the web

# **Automate file download in Python**
# ```python
# from urllib.request import urlretrieve 
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/ winequality-white.csv' 
# urlretrieve(url, 'winequality-white.csv')
# 
# ```

# **Using Pandas**
# ```python
# import pandas as pd
# 
# df = pd.read_csv(url,sep=';')
# ```

# ### HTTP requests to import files from the web

# **GET requests using urllib**
# ```python
# from urllib.request import urlopen, Request 
# url = "https://www.wikipedia.org/" 
# request = Request(url) 
# response = urlopen(request) 
# html = response.read() 
# response.close()
# 
# ```

# **GET requests using requests**
# ```python
# import requests 
# url = "https://www.wikipedia.org/" 
# r = requests.get(url) 
# text = r.text 
# ```

# ### Scraping the web in Python

# **BeautifulSoup**
# ```python
# from bs4 import BeautifulSoup 
# import requests 
# 
# url = 'https://www.crummy.com/software/BeautifulSoup/' 
# 
# r = requests.get(url) 
# 
# html_doc = r.text 
# 
# soup = BeautifulSoup(html_doc)
# 
# print(soup.prettify()) 
# 
# print(soup.title) 
# 
# print(soup.get_text())
# 
# for link in soup.find_all('a'):     
#     print(link.get('href'))
# ```

# ### Introduction to APIs and JSONs

# **Loading JSONs in Python**
# ```python
# import json 
# with open('snakes.json', 'r') as json_file:         
#     json_data = json.load(json_file)
#     
# for key, value in json_data.items():     
#     print(key + ':', value) 
# ```

# **Connecting to an API in Python**
# ```python
# import requests 
# url = 'http://www.omdbapi.com/?t=hackers' #?t=hackers query string 
# r = requests.get(url) 
# json_data = r.json() 
# for key, value in json_data.items():     
#     print(key + ':', value) 
# ```

# ### Twitter API

# **Authentication handler**
# ```python
# import tweepy, json  
# access_token = "..." 
# access_token_secret = "..." 
# consumer_key = "..." 
# consumer_secret = "..."   
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# auth.set_access_token(access_token, access_token_secret) 
# ```

# **Define stream listener class**
# ```python
# class MyStreamListener(tweepy.StreamListener):     
#     def __init__(self, api=None):         
#         super(MyStreamListener, self).__init__()         
#         self.num_tweets = 0         
#         self.file = open("tweets.txt", "w")     
#     def on_status(self, status):         
#         tweet = status._json 
#         self.file.write(json.dumps(tweet) + '\\n')         
#         tweet_list.append(status)         
#         self.num_tweets += 1         
#         if self.num_tweets < 100:             
#             return True         
#         else:             
#             return False         
#         self.file.close()  
# ```

# **Stream tweets**
# ```python
# # Create Streaming object and authenticate 
# l = MyStreamListener() 
# stream = tweepy.Stream(auth, l)   
# # This line filters Twitter Streams to capture data by keywords: 
# stream.filter(track=['apples', 'oranges']) 
# 
# ```
