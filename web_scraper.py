# TODO: Remove Twitter libraries
from typing import Dict, Literal
import snscrape.modules.twitter as sn
#import pandas as pd
import datetime
from preprocess import Preproccessor
from enum import Enum
# Before numpy: 55682971337
# After:        53477174548
# With dict:    51322316259
# With numpy: 
# TODO: improve space complexity

class ProcessingFlag(Enum):
    VADERIZE = 'V'
    TOKENIZE = 'T'

class WebScraper:
    def __init__(self):
        self.search_string = self._create_search_string()
        self.tweet_generator = self._create_generator(self.search_string)
        self.preprocessor = Preproccessor()
        self.tweet_storage = self._create_tweet_dict(self.tweet_generator)
        self.tweets_processed = False
        self.prompt_preprocess()

    # TODO: error handling
    def prompt_preprocess(self):
        processing_type = input("Preprocessing type(t/v):  ").lower()
        if processing_type == 't':
            self.preprocess_tweets(ProcessingFlag.TOKENIZE.value)
        elif processing_type == 'v':
            self.preprocess_tweets(ProcessingFlag.VADERIZE.value)
        else:
            raise
    # TODO: Custom exceptions for if already processed
    def preprocess_tweets(self, p_flag):
        if self.tweets_processed == False:
            if p_flag == 'T':
                self.tweet_storage.update((k,[date_tweet[0],self.preprocessor.tokenize_preprocess(date_tweet[1])]) for k,date_tweet in self.tweet_storage.items())
            elif p_flag == 'V':
                self.tweet_storage.update((k,[date_tweet[0],self.preprocessor.vader_preprocess(date_tweet[1])]) for k,date_tweet in self.tweet_storage.items())
            self.tweets_processed = True
        else:
            raise
        
    def get_tweet_storage(self):
        return self.tweet_storage

    def _prompt_start_date(self) -> str:
        while True:
            try:
                start_year = int(input("Start year: "))
                start_month = int(input("Start month: "))
                start_day = int(input("Start day: "))
                break
            except ValueError:
                raise ValueError('Must be an integer')
        return f"{start_year}-{start_month}-{start_day}"

    def _create_search_string(self) -> str:
        phrase = str(input("Phrase to search: "))
        #start_date = input("Start year: ") +'-'+ input("Start month: ") +'-'+ input("Start day: ")
        start_date = self._prompt_start_date()
        #end_date = input("End year: ") +'-'+ input("End month: ") +'-'+ input("End day: ")
        end_date = f"{datetime.datetime.now():%Y-%m-%d}"
        search_phrase = f"{phrase} since:{start_date} until:{end_date}"
        #print(f"Your search phrase is \'{search_phrase}\'")
        return search_phrase

    def _prompt_count(self) -> int:
        while True:
            try:
                store_num = int(input("Tweets to store: "))
                break
            except ValueError:
                raise ValueError('Must be an integer')
        return store_num 

    def _create_generator(self,search_phrase:str):
        return sn.TwitterSearchScraper(search_phrase).get_items() 

    # TODO: parallel/ improved time
    def _create_tweet_dict(self,tweet_generator) -> dict:
        count = self._prompt_count()
        tweet_dict = {}
        for i,tweet in enumerate(tweet_generator):
            if tweet.lang == 'en':
                tweet_dict[i] = [tweet.date, tweet.renderedContent]
            if i>= count:
                break
        return tweet_dict 
    
    # Dataframe was changed out for dict.
    #def _create_tweet_dataframe(self, tweet_generator):
    #    count = self._prompt_count()
    #    tweet_list = [] * count
    #    for i,tweet in enumerate(tweet_generator):
    #        if tweet.lang == 'en':
    #            #rendered_token = preprocessor.preprocess(tweet.renderedContent) 
    #            #tweet_list.append([tweet.date, rendered_token])
    #            tweet_list.append([tweet.date, tweet.renderedContent])
    #        if i >= count:
    #            break
    #    tweet_dataframe = pd.DataFrame(data=tweet_list,columns=['Date','Content'])
    #    # Converting Date-Time-Zone to Date-Time, Removing empty entries
    #    tweet_dataframe['Date'] = pd.to_datetime(tweet_dataframe['Date'])
    #    tweet_dataframe['Date'] = tweet_dataframe['Date'].dt.tz_localize(None)
    #    tweet_dataframe.dropna(inplace=True)
    #    return tweet_dataframe 

    def _print_tweets(self, tweet_generator):
        n = int(input("Tweets to print: "))
        print(f"You are printing {n} tweets\n")
        new_line = '\n'
        for i,tweet in enumerate(tweet_generator):
            if (tweet.lang == 'en'):
                print(f"{tweet.date}:{tweet.renderedContent} {new_line}")
            if (i >= n):
                break

    def __str__(self) -> str:
        return f"{self.tweet_storage}"


#def main():
#    search_phrase = search_string()
#    tweet_generator = _create_generator(search_phrase)
#    if input("Print(y/n)?: ") == 'y':
#        _print_tweets(tweet_generator)
#    if input("Store as excel(y/n)?: ") == 'y':
#        store_count = int(input("Tweets to store: "))
#        start = time.perf_counter_ns()
#        tweet_dataframe = create_tweet_dataframe(tweet_generator,store_count)
#        # tweet_dict = _create_tokenized_tweet_dict(tweet_generator,store_count)
#        end = time.perf_counter_ns()
#        print("Time to create dataframe: ",end - start)
#        print(tweet_dataframe.to_string())
#        #tweet_dataframe.to_excel(f"./rsc/{search_phrase}x{store_count}.xlsx") 
## TODO: Improve space complexity
#if __name__ == "__main__":
#    main()
