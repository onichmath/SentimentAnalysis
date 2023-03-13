# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import sys

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

def _create_tweet_list(n,tweet_generator):
    tweet_list = []
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            tweet_list.append([tweet.date, tweet.rawContent])
            n -= 1
        if n < 1:
            break
    return tweet_list


if __name__ == "__main__":
    tweet_generator = _prompt_search()
    print(sys.getsizeof(tweet_generator))
    _print_tweets(tweet_generator)
    tweet_list = _create_tweet_list(int(input("Tweets to store: ")),tweet_generator)
    sys.getsizeof(tweet_list)

