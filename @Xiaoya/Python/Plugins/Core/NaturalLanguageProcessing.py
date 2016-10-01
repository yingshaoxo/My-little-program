import os
import nltk


global path
path = os.path.dirname(__file__) + '\\'

class NaturalLanguageProcessing():

    def sentences_segment(self, text):
        sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return sent_tokenizer.tokenize(text)

    def word_tokenize_1(self, text):
        return nltk.word_tokenize(text)

    def word_tokenize_2(self, text):
        from nltk.tokenize import WordPunctTokenizer
        return WordPunctTokenizer().tokenize(text)

    def word_tokenize_3(self, text):
        pattern = r"""(?x)                   # set flag to allow verbose regexps
                        (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                        |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                        |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                        |\.\.\.                # ellipsis
                        |(?:[.,;"'?():-_`])    # special characters with meanings
                        """
        return nltk.regexp_tokenize(text, pattern)

    #CC--Coordinating conjunction, RB--Adverb, IN--Preposition or subordinating conjunction
    #NN--Noun, singular or mass, JJ--Adjective, VB--Verb, base form
    def tag(self, text):
        words = self.word_tokenize_1(text)
        return nltk.pos_tag(words)

    def remove_tag(self, tagged_list):
        return [item[0] for item in tagged_list]

    #['RB', 'JJ', 'NN', 'VB'], 5
    def filter_some_types(self, tagged_list, maintain_types_list):
        return [a_tuple for a_tuple in tagged_list if a_tuple[1] in maintain_types_list]

    def filter_from_length(self, tagged_list, min_length_limit):
        return [a_tuple for a_tuple in tagged_list if len(a_tuple[0]) >= 5]

    def frequency_dict(self, text, num_limit):
        from nltk.probability import FreqDist
        fdist = FreqDist(self.word_tokenize_1(text))
        return sorted(fdist.items(), key=lambda fdist: fdist[1], reverse=True)[:num_limit]

    def remove_duplicates(self, words_list):
        return list(set(words_list))

    def only_english(seld, words_list):
        english_set = set(w.lower() for w in nltk.corpus.words.words())
        return [word.lower() for word in words_list if word.lower() in english_set]

    def stem(self, vocabulary):
        porter = nltk.PorterStemmer()
        return porter.stem(vocabulary)

    def filter_from_list(self, word_list, filter_list):
        word_list = [word.lower() for word in word_list]
        filter_list = [word.lower() for word in filter_list]
        return [word for word in word_list if word not in filter_list]

def organize_text(text):
    while text[0:1] == '\n' or text[0:1] == ' ':
        text = text[1:]
    while text[-1:] == '\n' or text[-1:] == ' ':
        text = text[:-1]
    return text

def youdao_translate(text):
    import requests
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' + text, \
                     headers = {
    'User-Agent': 'translator/2.2.0(Android/4.4.4/zh_CN;HM NOTE 1S)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'fanyi.youdao.com',
    'Connection': 'Keep-Alive'
})
    translation = r.text.split('result=')[1][:-1]
    return text + '\n' + translation

def all_translate(words_list):
    result = ''
    for word in words_list:
        result += youdao_translate(word) + '\n\n'
    result = organize_text(result)
    return result

def from_ariticle_get_word(text):
    with open(path + '/OtherNeeded/simple_word.txt', 'r') as f:
    	simple_word = f.read()
    filter_list = eval(simple_word)
    #text = '''Readers happily accepted the fact that an obscure maidservant was really the hero's mother.'''
    try:
        a = NaturalLanguageProcessing()
        tagged = a.tag(text)
        filtered1 = a.filter_some_types(tagged, ['RB', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'])
        filtered2 = a.filter_from_length(filtered1, 5)
        removed1 = a.remove_tag(filtered2)
        removed2 = a.remove_duplicates(removed1)
        filtered3 = a.filter_from_list(removed2, filter_list)
        result = a.only_english(filtered3)
        result = all_translate(result)
        return result
    except Exception as e:
        return e

#print(from_ariticle_get_word('''Readers happily accepted the fact that an obscure maidservant was really the hero's mother.'''))

#test
'''
a = NaturalLanguageProcessing()
tagged = a.tag(text)
filtered1 = a.filter_some_types(tagged, ['RB', 'JJ', 'NN', 'VB'])
filtered2 = a.filter_from_length(filtered1, 5)
removed1 = a.remove_tag(filtered2)
removed2 = a.remove_duplicates(removed1)
filtered3 = a.filter_from_list(removed2, filter_list)
result = a.only_english(filtered3)
result = all_translate(result)
print(result)
'''

#get filter list
'''
with open('All text.txt', 'rt') as f:
    text = f.read()

a = NaturalLanguageProcessing()
b = a.frequency_dict(text, -1)
c = a.filter_from_length(b, 5)
result = a.remove_duplicates(a.remove_tag(c))
result = a.only_english(result)

print(len(result))
for num, word in enumerate(result):
    print(str(num) + ' ', word)

with open('result.txt', 'wt') as f:
    f.write(str(result))
'''
