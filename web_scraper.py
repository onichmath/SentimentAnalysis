# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import sys

# TODO: numpy list
# TODO: start and end times for scraping
def _prompt_search():
    search_phrase = input("Phrase to search: ")
    tweet_generator = sn.TwitterSearchScraper(search_phrase+" since 2023-03-12").get_items()
    return tweet_generator

def _print_tweets(tweet_generator):
    i = int(input("Tweets to print: "))
    print(f"You are printing {i} tweets\n")
    new_line = '\n'
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            print(f"{tweet.date} {tweet.rawContent} {new_line}")
            i-=1
        if (i < 1):
            break

def _create_tweet_list(tweet_generator):
    tweet_list = []
    n = int(input("Tweets to store: "))
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
    if input("Print(y/n)?: ") == 'y':
        _print_tweets(tweet_generator)
    if input("Store(y/n)?: ") == 'y':
        tweet_list = _create_tweet_list(tweet_generator)
        tweet_dataframe = pd.DataFrame(tweet_list)
        # TODO: relative filepath
        tweet_dataframe.to_excel("/home/matthewo/Documents/Projects/SentimentAnalysis/res/tweet.xlsx")
