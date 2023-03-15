# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import sys
import datetime

# TODO: numpy list
# TODO: improve space complexity
# TODO: Store generator instead of dataframe
def _search_string():
    phrase = str(input("Phrase to search: "))
    start_date = input("Start year: ") +'-'+ input("Start month: ") +'-'+ input("Start day: ")
    end_date = f"{datetime.datetime.now():%Y-%m-%d}"
    search_phrase = f"{phrase} since:{start_date} until:{end_date}"
    print(f"Your search phrase is \'{search_phrase}\'")
    return search_phrase

def _prompt_search(search_phrase):
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

# TODO: Append date with scrubbed timezone
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
    search_phrase = _search_string()
    tweet_generator = _prompt_search(search_phrase)
    if input("Print(y/n)?: ") == 'y':
        _print_tweets(tweet_generator)
    if input("Store as excel(y/n)?: ") == 'y': 
        tweet_list = _create_tweet_list(tweet_generator)
        tweet_dataframe = pd.DataFrame(data=tweet_list,columns=['Content'])
        tweet_dataframe.to_excel(f"./rsc/{search_phrase}.xlsx")
