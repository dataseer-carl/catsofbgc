import pandas as pd
import tweepy
from bs4 import BeautifulSoup
import requests
import re
import json
import os

twitter_key = 'MaHlAawYWyfRUfxQdeROW0SnK'
twitter_secret = 'i7u2bzOt2YWtqWUfMCuwvD2W0u7M03T21ST1jMhllOsJPfXtV9'


twitter_access_token = '143080936-Fn9ty2d3wDSkstugNF3kwsuakDwseEpV8ub1GNyK'
twitter_access_secret = '44szAzBhgaGywuibpldzI1yk2yU2YSLOLAKIEirk5X2W2'


auth = tweepy.OAuthHandler(
    twitter_key,
    twitter_secret)

auth.set_access_token(twitter_access_token, twitter_access_secret)

twitter_api = tweepy.API(auth)

MAX_T = 5000000000000000000000

tweets_df = []
hashtag_tweets_df = []

for tweet in tweepy.Cursor(
    twitter_api.search,
    q='cats of bgc',
        rpp=100).items(MAX_T):
    tweets_df.append(tweet._json)

for tweet in tweepy.Cursor(
    twitter_api.search,
    q='#catsofbgc',
        rpp=100).items(MAX_T):
    hashtag_tweets_df.append(tweet._json)

tweets_df.extend(hashtag_tweets_df)

cat_dict = {c: post for c, post in enumerate(tweets_df)}

with open('twitter_raw.json', 'w') as raw:
    raw.write(json.dumps(cat_dict))

source_tweets = []
rt_tweets = []

for tweet in tweets_df:
        if 'retweeted_status' not in tweet.keys():
            source_tweets.append(tweet)
        else:
            rt_tweets.append(tweet)


def truncated_text(text):
    link = re.findall('https?[^ ]+', text)[-1]

    url = re.search(
        '^https?://([a-zA-Z-.]+)',
        requests.head(
            link,
            allow_redirects=True).url).group(1).lower()

    if re.search('facebook', url):
        to_return = 'facebook'
    elif re.search('instagram', url):
        to_return = 'instagram'
    elif re.search('twitter', url):
        html = requests.get(link)
        soup = BeautifulSoup(html.text, 'html.parser')
        for a in soup.find('p', class_='TweetTextSize').find_all('a'):
            a.decompose()

        to_return = soup.find('p', class_='TweetTextSize').text
    else:
        to_return = re.sub('https?[^ ]+', '', text).strip()

    return to_return


final_tweets = []

for c, tweet in enumerate(source_tweets):
    print(f'{c}: Processing Data Point...')
    id_str = tweet['id_str']
    if not tweet['truncated'] and 'http' not in tweet['text']:
        text = tweet['text']
    else:
        text = truncated_text(tweet['text'])

    final_tweets.append(text)


def tweet_link(code):
    return f'https://twitter.com/i/web/status/{code}'


created_at = [tweet['created_at'] for tweet in source_tweets]
links = [tweet_link(tweet['id']) for tweet in source_tweets]

main_tweet_df = pd.DataFrame(
    {'text': final_tweets,
     'time': created_at,
     'link': links})

main_tweet_df = main_tweet_df.loc[main_tweet_df.text != 'instagram']

with pd.HDFStore('cats_of_bgc.h5') as hdf:
    hdf.put(key='twitter', value=main_tweet_df)
