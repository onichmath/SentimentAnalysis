# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import sys
import datetime
import pickle

#TODO: deserialize generator to store generator object in file
# TODO: numpy list
# TODO: start and end times for scraping
# TODO: improve space complexity
# TODO: Store generator instead of dataframe
def _prompt_search():
    phrase = str(input("Phrase to search: "))
    start_date = input("Start year: ") +'-'+ input("Start month: ") +'-'+ input("Start day: ")
    end_date = f"{datetime.datetime.now():%Y-%m-%d}"
    search_phrase = f"{phrase} since:{start_date} until:{end_date}"
    print(f"Your search phrase is \'{search_phrase}\'")
    # TODO: Fix giant error creating generator
    tweet_generator = sn.TwitterSearchScraper(search_phrase).get_items() 
    return tweet_generator

def _print_tweets(tweet_generator):
    n = int(input("Tweets to print: "))
    print(f"You are printing {n} tweets\n")
    new_line = '\n'
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            print(f"{tweet.renderedContent} {new_line}")
        if (i >= n):
            break


# TODO: Datetimezone to datetime in createtweet method
def _create_tweet_list(tweet_generator):
    tweet_list = []
    n = int(input("Tweets to store: "))
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            tweet_list.append([tweet.renderedContent])
        if i >= n:
            break
    return tweet_list

if __name__ == "__main__":
    tweet_generator = _prompt_search()
    #print(sys.getsizeof(tweet_generator))
    if input("Print(y/n)?: ") == 'y':
        _print_tweets(tweet_generator)
    if input("Store as excel(y/n)?: ") == 'y':
        tweet_list = _create_tweet_list(tweet_generator)
        tweet_dataframe = pd.DataFrame(data=tweet_list,columns=['Content'])
        # Convertine date time to date for excel compatibility
        #tweet_dataframe['Date'].dt.tz_convert(None)
        #tweet_dataframe['date'] = tweet_dataframe['date'].apply(lambda x: pd.to_datetime(x).date())
        # TODO: relative filepath
        tweet_dataframe.to_excel("/home/matthewo/Documents/Projects/SentimentAnalysis/res/tweet.xlsx")
