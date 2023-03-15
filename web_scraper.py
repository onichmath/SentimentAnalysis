# TODO: Remove Twitter libraries
import snscrape.modules.twitter as sn
import pandas as pd
import datetime
import time
import numpy as np
# Before numpy: 55682971337
# After:        53477174548
# TODO: numpy list
# TODO: improve space complexity
# TODO: Store generator instead of dataframe
def _search_string():
    phrase = str(input("Phrase to search: "))
    start_date = input("Start year: ") +'-'+ input("Start month: ") +'-'+ input("Start day: ")
    #end_date = input("End year: ") +'-'+ input("End month: ") +'-'+ input("End day: ")
    end_date = f"{datetime.datetime.now():%Y-%m-%d}"
    search_phrase = f"{phrase} since:{start_date} until:{end_date}"
    print(f"Your search phrase is \'{search_phrase}\'")
    return search_phrase

def _create_generator(search_phrase):
    tweet_generator = sn.TwitterSearchScraper(search_phrase).get_items() 
    return tweet_generator

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
def _create_tweet_dataframe(tweet_generator,count):
    #tweet_dataframe = np.fromiter(tweet_generator, dtype=sn.Tweet, count=count)
    #return tweet_dataframe
    tweet_list = [] * count
    for i,tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            #tweet.date = tweet.date.replace(tzinfo=None)
            tweet_list.append([tweet.date, tweet.renderedContent])
        if i >= count:
            break
    tweet_dataframe = pd.DataFrame(data=tweet_list,columns=['Date','Content'])
    # Converting Date-Time-Zone to Date-Time
    tweet_dataframe['Date'] = pd.to_datetime(tweet_dataframe['Date'])
    tweet_dataframe['Date'] = tweet_dataframe['Date'].dt.tz_localize(None)
    return tweet_dataframe 

# TODO: Improve space complexity
if __name__ == "__main__":
    search_phrase = _search_string()
    tweet_generator = _create_generator(search_phrase)
    if input("Print(y/n)?: ") == 'y':
        _print_tweets(tweet_generator)
    if input("Store as excel(y/n)?: ") == 'y':
        store_count = int(input("Tweets to store: "))
        start = time.perf_counter_ns()
        tweet_dataframe = _create_tweet_dataframe(tweet_generator,store_count)
        end = time.perf_counter_ns()
        print("Time to create dataframe: ",end - start)
        tweet_dataframe.to_excel(f"./rsc/{search_phrase}x{store_count}.xlsx")
        
