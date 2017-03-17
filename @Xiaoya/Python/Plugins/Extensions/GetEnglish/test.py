import requests
import json
import time
import os
import re


def OrganizeText(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　'):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　'):#right
        text = text[:-1]
    return text


def youdao_translate1(text):
    headers = {'Host': 'fanyi.youdao.com', 'User-Agent': 'translator/2.2.0(Android/4.4.4/en_US;HM NOTE 1S)', 'Content-Type': 'application/x-www-form-urlencoded'}
    body = 'q='+ text +'&doctype=json&imei=867822021478135&screen=720x1280&model=HM_NOTE_1S&mid=4.4.4&version=2.2.0&vendor=googleplay&keyfrom=fanyi.2.2.0.android' #&type=EN2ZH_CN
    r = requests.post('http://fanyi.youdao.com/appapi/translate?&model=HM_NOTE_1S&mid=4.4.4&imei=867822021478135&vendor=googleplay&screen=720x1280&version=2.2.0&keyfrom=fanyi.2.2.0.android', headers=headers, data=body, timeout=10)

    text = r.text
    big_dict = json.loads(text)

    try:
        fanyi_dict = big_dict.get('fanyi')
        r_fanyi = fanyi_dict.get('org') + '\n' + fanyi_dict.get('trans')
        r_fanyi = OrganizeText(r_fanyi)
    except:
        r_fanyi = ''
    
    try:
        dict_dict = big_dict.get('dict')
        r_dict = dict_dict.get('org')  + '\n'
        for i in dict_dict.get('phrases'):
            r_dict += i + '\n'
        r_dict = r_dict[0:len(r_dict)+1-2]
        r_dict = OrganizeText(r_dict)
    except:
        r_dict = ''

    try:
        sentence_list = big_dict.get('sentence')
        r_sentence = ''
        for i in sentence_list:
            i_dict = dict(i)
            r_sentence += i_dict.get('org') + '\n' + i_dict.get('trans') +'\n\n'
        r_sentence = r_sentence.replace('<b>','').replace('</b>','')
        r_sentence = r_sentence.split('<br><br>')[0]
        r_sentence = OrganizeText(r_sentence)
    except:
        r_sentence = ''

    result = ''
    for i in [r_fanyi, r_dict, r_sentence]:
        if i != '':
            result += i + '\n\n\n'
    result = OrganizeText(result)

    return result



def youdao_translate2(text):
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' \
     + text)
    translation = r.text.split('result=')[1][:-2]
    return text + '\n' + translation


with open('result.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for i in sorted(list(set([i for i in text.split('\n\n——————————————\n\n') if i not in ['\n', '', ' ']]))):
    with open('r2.txt', 'a', encoding='utf-8') as f:
        f.write(i + '\n\n——————————————\n\n')

print('OK')
#print(youdao_translate1('sky'))
