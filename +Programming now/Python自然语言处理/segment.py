"""
How to use it?

First, pip install nltk

Second:
    import nltk
    nltk.download() # It'll open a window, just download all Packages!
    
Then you can run the following codes
"""

import nltk


def sentences_segment(text):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_tokenizer.tokenize(text)
    return sentences

def get_words1(text):
    from nltk.tokenize import WordPunctTokenizer
    words = WordPunctTokenizer().tokenize(text)
    return words


def get_words2(text):
    pattern = r"""(?x)                   # set flag to allow verbose regexps 
              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A. 
              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages 
              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
              |\.\.\.                # ellipsis 
              |(?:[.,;"'?():-_`])    # special characters with meanings 
            """  
    words = nltk.regexp_tokenize(text, pattern)
    return words


text = "How it came about that snakes manufactured poison is a mystery. Over the periods their saliva, a mild, digestive juice like our own, was converted into a poison that defies analysis even today."
print(get_words1(text))
