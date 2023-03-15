# TODO: Remove Twitter libraries
from pandas.core.computation.parsing import tokenize
import snscrape.modules.twitter as sn
import pandas as pd
import datetime
import time
import numpy as np
from nltk.tokenize import word_tokenize
# Before numpy: 55682971337
# After:        53477174548
# With dict:    51322316259
# With numpy: 
# TODO: numpy list
# TODO: improve space complexity
# TODO: Store generator instead of dataframe
# TOOD: scrape and tokenize into numpy array
def main():
    search_phrase = _search_string()
    tweet_generator = _create_generator(search_phrase)
    if input("Print(y/n)?: ") == 'y':
        _print_tweets(tweet_generator)
    if input("Store as excel(y/n)?: ") == 'y':
        store_count = int(input("Tweets to store: "))
        start = time.perf_counter_ns()
        tweet_dataframe = _create_tweet_dataframe(tweet_generator,store_count)
        #tweet_dict = _create_tokenized_tweet_dict(tweet_generator,store_count)
        #tweet_array = _create_tweet_nparray(tweet_generator,store_count)
        end = time.perf_counter_ns()
        print("Time to create dataframe: ",end - start)
        #tweet_dataframe.to_excel(f"./rsc/{search_phrase}x{store_count}.xlsx") 

def _tokenize(tweet_content):
    tokens = word_tokenize(tweet_content)
    lcase_nopunc_tokens = [token.lower() for token in tokens]
    return lcase_nopunc_tokens

def _search_string():
    phrase = str(input("Phrase to search: "))
    start_date = input("Start year: ") +'-'+ input("Start month: ") +'-'+ input("Start day: ")
    #end_date = input("End year: ") +'-'+ input("End month: ") +'-'+ input("End day: ")
    end_date = f"{datetime.datetime.now():%Y-%m-%d}"
    search_phrase = f"{phrase} since:{start_date} until:{end_date}"
    print(f"Your search phrase is \'{search_phrase}\'")
    return search_phrase

def _create_generator(search_phrase):
    return sn.TwitterSearchScraper(search_phrase).get_items() 

def _print_tweets(tweet_generator):
    n = int(input("Tweets to print: "))
    print(f"You are printing {n} tweets\n")
    new_line = '\n'
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            print(f"{tweet.date}:{tweet.renderedContent} {new_line}")
        if (i >= n):
            break

# TODO: Append date with scrubbed timezone
# TODO: parallel/ improved time
# TODO: tokenize and insert raw content into numpy array instead of creating dataframe
def _create_tokenized_tweet_dict(tweet_generator,count):
    tweet_dict = {}
    for i,tweet in enumerate(tweet_generator):
        if tweet.lang == 'en':
            tweet_dict[i] = tweet.renderedContent
        if i>= count:
            break
    tweet_dict.update({k: _tokenize(v) for k,v in tweet_dict.items()})
    return tweet_dict 

def _create_tweet_dataframe(tweet_generator,count):
    tweet_list = [] * count
    for i,tweet in enumerate(tweet_generator):
        if tweet.lang == 'en':
            #tweet.date = tweet.date.replace(tzinfo=None)
            rendered_token = _tokenize(tweet.renderedContent) 
            tweet_list.append([tweet.date, rendered_token])
        if i >= count:
            break
    tweet_dataframe = pd.DataFrame(data=tweet_list,columns=['Date','Content'])
    # Converting Date-Time-Zone to Date-Time
    tweet_dataframe['Date'] = pd.to_datetime(tweet_dataframe['Date'])
    tweet_dataframe['Date'] = tweet_dataframe['Date'].dt.tz_localize(None)
    return tweet_dataframe 

# TODO: Improve space complexity
if __name__ == "__main__":
    main()
