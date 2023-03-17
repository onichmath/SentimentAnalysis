import snscrape.modules.twitter as sn

def get_tweet_list(phrase: str, count: int) -> list[str]:
    """
    Returns a list of tweets relating to the phrase with length <= count
    
    Parameters:
    phrase (str): The phrase to search for on twitter
    count (int): The number of tweets to return in the list

    Returns:
    list[str]: List of tweets with @s stripped
    """

    list_of_tweets = []
    tweet_generator = sn.TwitterSearchScraper(phrase).get_items()
    index = 0
    for tweet in tweet_generator:
        if index >= count:
            break
        if (tweet.lang == 'en'):
            list_of_tweets.append(remove_at(tweet.renderedContent.strip("\n")))
            index += 1
    return list_of_tweets

def remove_at(tweet: str) -> str:
    first_at = tweet.find('@')
    if first_at < 0:
        return tweet
    
    end_of_at = tweet[first_at:].find(' ')
    if end_of_at < 0:
        return tweet
    
    cleaned_tweet = tweet[:first_at].join(tweet[end_of_at + 1:])
    return remove_at(cleaned_tweet)