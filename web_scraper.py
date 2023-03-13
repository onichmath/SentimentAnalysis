# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import sys

tweet_list = []
# TODO: numpy list
# TODO: start and end times for scraping
def _prompt_search():
    search_phrase = input("Phrase to search: ")
    tweet_generator = sn.TwitterSearchScraper(search_phrase).get_items()
    return tweet_generator

def _print_tweets(tweet_generator):
    i = 0
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            print(tweet.vibe, tweet.date)
            i+=1
        if (i > 9):
            break

if __name__ == "__main__":
    tweet_generator = _prompt_search()
    print(sys.getsizeof(tweet_generator))
    _print_tweets(tweet_generator)
