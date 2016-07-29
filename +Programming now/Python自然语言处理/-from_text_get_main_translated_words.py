#import nltk
#PorterStemmer
#英文词干提取
#def stem(vocabulary):
#    porter = nltk.PorterStemmer()
#    return porter.stem(vocabulary)


import nltk

#tag text
#词性标注
def tag(text):
    words = nltk.word_tokenize(text)
    return nltk.pos_tag(words)    #CC是连接词，RB是副词，IN是介词，NN是名次，JJ是形容词，VB是动词

#filter
#过滤
def filter_some_types(tagged_list):
    def judge(a_tuple_in_list):
        word_type  = a_tuple_in_list[1]
        if word_type.count('RB') >= 1 or word_type.count('JJ') >= 1 or word_type.count('NN') >= 1 \
           or (word_type.count('VB') >= 1):  #  and word_type.count('P') == 0 and word_type.count('Z') == 0
            if len(a_tuple_in_list[0]) > 5:
                return True
    new_tagged_list = list(filter(judge, tagged_list))
    return new_tagged_list

def filter_some_types2(tagged_list, maintain_types_list, min_length_limit):
    def judge(a_tuple):
        for type_ in maintain_types_list:
            if a_tuple[1].count(type_) >= 1:
                if len(a_tuple[0]) > min_length_limit:
                    return True
    return list(filter(judge, tagged_list))


def get_words_list(tagged_list):
    return [item[0] for item in tagged_list]




def youdao_translate2(text):
    import requests
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' \
     + text)
    translation = r.text.split('result=')[1][:-1]
    return text + '\n' + translation




def organize_text(text):
    while (text[0:1] == '\n' or text[0:1] == ' '):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' '):#right
        text = text[:-1]
    return text

def all_translate(words_list):
    result = ''
    for word in words_list:
        result += youdao_translate2(word) + '\n\n'
    result = organize_text(result)
    return result

def from_text_get_main_translated_words(text):
    return all_translate(get_words_list(filter_some_types2(tag(text), ['RB', 'JJ', 'NN', 'VB'], 5)))



text = """In the early days of the settlement of Australia, enterprising settlers unwisely
introduced the European rabbit. This rabbit had no natural enemies in the Antipodes,
so that it multiplied with that promiscuous abandon characteristic of
rabbits. It overran a whole continent. It caused devastation by burrowing and
by devouring the herbage which might have maintained millions of sheep and
cattle."""
text2 = '''It overran a whole continent. It caused devastation by burrowing and
by devouring the herbage which might have maintained millions of sheep and
cattle.'''

print(from_text_get_main_translated_words(text2))
