from hashlib import md5
import requests
import random
import json
import re


def OrganizeText(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　' or text[0:1] == ' '):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　' or text[-1:] == ' '):#right
        text = text[:-1]
    text = text.strip('  　\n ')
        
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

def baidu_translate(text):
    appid = '20160212000011684'
    secretKey = 'Mpbkg9bCYzBrc74HWlkX'
 
    q = text
    fromLang = 'en'
    toLang = 'zh'
    salt = 520

    sign = appid+q+str(salt)+secretKey
    m1 = md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate?q='+q+'&from='+fromLang+'&to='+toLang+'&appid='+appid+'&salt='+str(salt)+'&sign='+sign
 
    try:
        r = requests.get(myurl)
        rr =  json.loads(r.text)['trans_result'][0]['dst']
        return rr
    except Exception as e:
        print (e)

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
                result += baidu_translate(sentence)
        except:
            result += sentence
        if num != len(sentence_lists)-1:
            result += '\n' * 2
        else:
            result += '\n' * 2
    return OrganizeText(result)
#"""
text = '''
When I was 13 my only purpose was to become the star on our football team.

That meant beating out Miller King, who was the best player at our school.

Football season started in September and all summer long I worked out.

I carried my football everywhere for practice.

Just before September, Miller was struck by a car and lost his right arm.

I went to see him after he came back from hospital.

He looked very pale, but he didn't cry.

That season, I broke all of Miller's records while he watched the home games from the bench.

We went 10-1 and I was named most valuable player, but I often had crazy dreams in which I was to blame for Miller's accident.

One afternoon, I was crossing the field to go home and saw Miller stuck going over a fence — which wasn't hard to climb if you had both arms.

I'm sure I was the last person in the world he wanted to accept assistance from.

But even that challenge he accepted.

I helped him move slowly over the fence.

When we were finally safe on the other side, he said to me, "You know, I didn't tell you this during the season, but you did fine. Thank you for filling in for me."

His words freed me from my bad dreams.

I thought to myself, how even without an arm he was more of a leader.

Damaged but not defeated, he was still ahead of me.

I was right to have admired him.

From that day on, I grew bigger and a little more real.

'''
text = OrganizeText(text).replace('\n\n','\n')
with open('article.txt', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(main(text))
print('OK~')
#"""
