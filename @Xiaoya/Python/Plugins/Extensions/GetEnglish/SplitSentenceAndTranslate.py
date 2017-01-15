import requests
import random
import re


def OrganizeText(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　' or text[0:1] == ' '):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　' or text[-1:] == ' '):#right
        text = text[:-1]
        
    return text

def SplitSentences(text):
    text = OrganizeText(text)
    
    text = text.replace('. ', '.\n')
    text = text.replace('? ', '?\n')
    text = text.replace('! ', '!\n')
    text = text.replace('; ', ';\n')
    
    if text.count('\n')<5:
        text = text.replace('. ', '.\n')
        text = text.replace('? ', '?\n')
        text = text.replace('! ', '!\n')
        text = text.replace('; ', ';\n')
    
    text = OrganizeText(text)
    sentences_list = text.split('\n')
    all_sentences = ''
    for num, each in enumerate(sentences_list, start=0):
        one_sentence = OrganizeText(each)
        sentences_list[num] = one_sentence
        all_sentences += one_sentence
        
    return sentences_list

def youdao_translate(text):
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' \
     + text)
    translation = r.text.split('result=')[1][:-2]
    return text + '\n' + translation

def google_translate(text):
    requests.packages.urllib3.disable_warnings()
    r = requests.get('http://translate.google.cn/translate_a/t?client=j&text=' + text + '&hl=zh-CN&multires=1&otf=1&pc=0&sc=1&sl=en&tl=zh-CN', verify=False)
    translation = r.text[1:-1]
    if translation.find('!DOCTYPE') == -1:
        return text + '\n' + translation
    else:
        return youdao_translate(text)

'''
def main(msg):
    result = google_translate(msg)
    return result'''
def main(msg):
    text = msg
    text = OrganizeText(text)
    sentence_lists = SplitSentences(text)
    result = ''
    for num, sentence in enumerate(sentence_lists, start=0):
        try:
            if random.randrange(0, 1) == 0:
                result += google_translate(sentence)
            else:
                result += youdao_translate(sentence)
        except:
            result += sentence
        if num != len(sentence_lists)-1:
            result += '\n' * 2
        else:
            result += '\n' * 2
    return result

#print(google_translate('yes'))
