import nltk

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
    def filter_some_types(self, tagged_list, maintain_types_list, min_length_limit):
        def judge(a_tuple):
            for type_ in maintain_types_list:
                if a_tuple[1].count(type_) >= 1:
                    if len(a_tuple[0]) > min_length_limit:
                        return True
        return list(filter(judge, tagged_list))


def organize_text(text):
    while (text[0:1] == '\n' or text[0:1] == ' '):
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' '):
        text = text[:-1]
    return text

def youdao_translate(text):
    import requests
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' \
     + text)
    translation = r.text.split('result=')[1][:-1]
    return text + '\n' + translation

def all_translate(words_list):
    result = ''
    for word in words_list:
        result += youdao_translate(word) + '\n\n'
    result = organize_text(result)
    return result

def remove_duplicates(words_list):
    return list(set(words_list))


text='''*527*your text*527*'''
try:
    a = NaturalLanguageProcessing()
    tagged = a.tag(text)
    filtered = a.filter_some_types(tagged, ['RB', 'JJ', 'NN', 'VB'], 5)
    removed1 = a.remove_tag(filtered)
    removed2 = remove_duplicates(removed1)
    result = all_translate(removed2)
    print(result)
except:
    print ('')
