import snscrape.modules.twitter as sn

def get_tweet_list(phrase: str, count: int) -> list:
    list_of_tweets = []
    tweet_generator = sn.TwitterSearchScraper(phrase).get_items()
    for index, tweet in enumerate(tweet_generator):
        if (tweet.lang == 'en'):
            print(f"Tweet by @{tweet.user.username} ({tweet.user.followersCount} followers) with {tweet.likeCount} likes: ", end="")
            print(tweet.renderedContent.strip("\n"))
            list_of_tweets.append(tweet.renderedContent.strip("\n"))
        if (index > count):
            break
    return list_of_tweets

