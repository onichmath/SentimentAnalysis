from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
#import SpellCheck

class Preproccessor:
    def __init__(self):
        self._regex_tokenizer = RegexpTokenizer(r'\w+\S+')

    def _rm_whitespace(self,tweet_content:str):
        return " ".join(tweet_content.split())

    def _spell_check(self,tweet_content:str):
        pass

    def preprocess(self,tweet_content: str):
        tokens = self._regex_tokenizer.tokenize(tweet_content)
        lcase_nopunc_tokens = [token.lower() for token in tokens if token not in list(stopwords.words('english'))]
        return lcase_nopunc_tokens


