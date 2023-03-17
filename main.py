"""
1. Prompt user for hashtag to scrape
With options for amount of data to scrape

2. Scrape data from twitter and store it into ?? file

3. Sentiment analysis on data

4. Display results, options for what to display
"""

from web_scraper import get_tweet_list

phrase = input("Type a phrase to search > ")
count = int(input("Enter the number of tweets > "))
tweets = get_tweet_list(phrase, count)
print(tweets)

for tweet in tweets:
    print(tweet)