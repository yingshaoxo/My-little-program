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
        
    return [i for i in sentences_list if i.strip('  　\n ')!='']

def handle_result(text):
    if ' ' in text:
        text = text.replace(',', '，').replace(';', '；')
        if "。" not in text[-6:]:
            text += '。'
        return text
    else:
        return text

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
        translation =  json.loads(r.text)['trans_result'][0]['dst']
        translation = handle_result(translation)
        return text + '\n' + translation
    except Exception as e:
        print (e)
        return ''

def google_translate(text):
    requests.packages.urllib3.disable_warnings()
    r = requests.get('http://translate.google.cn/translate_a/t?client=j&text=' + text + '&hl=zh-CN&multires=1&otf=1&pc=0&sc=1&sl=en&tl=zh-CN', verify=False)
    translation = r.text[1:-1]
    if translation.find('!DOCTYPE') == -1:
        translation = handle_result(translation)
        return text + '\n' + translation
    else:
        return baidu_translate(text)

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
                result += '\n' #baidu_translate(sentence)
        except:
            result += sentence
        if num != len(sentence_lists)-1:
            result += '\n' * 2
        else:
            result += ''
    return OrganizeText(result)
"""
text = '''
Good News Beats Bad on Social Networks.


Bad news sells.

If it bleeds, it leads.

No news is good news, and good news is no news.

Those are the classic rules for the evening broadcasts and the morning papers.

But now that information is being spread and monitored in different ways, researchers are discovering new rules.

By tracking people's e-mails and online posts, scientists have found that good news can spread faster and farther than disasters and sob stories.

"The 'if it bleeds' rule works for mass media," says Jonah Berger, a scholar at the University of Pennsylvania.

"They want your eyeballs and don't care how you're feeling. But when you share a story with your friends, you care a lot more how they react. You don't want them to think of you as a Debbie Downer."

Researchers analyzing word-of-mouth communication — e-mails, Web posts and reviews, face-to-face conversations — found that it tended to be more positive than negative, but that didn't necessarily mean people preferred positive news.

Was positive news shared more often simply because people experienced more good things than bad things?

To test for that possibility, Dr.Berger looked at how people spread a particular set of news stories: thousands of articles on The New York Times' website.

He and a Penn colleague analyzed the "most e-mailed" list for six months.

One of his first findings was that articles in the science section were much more likely to make the list than non-science articles.

He found that science amazed Times' readers and made them want to share this positive feeling with others.

Readers also tended to share articles that were exciting or funny, or that inspired negative feelings like anger or anxiety, but not articles that left them merely sad.

They needed to be aroused one way or the other, and they preferred good news to bad.

The more positive an article, the more likely it was to be shared, as Dr.Berger explains in his new book, "Contagious: Why Things Catch On."

'''
text = OrganizeText(text)
with open('article.txt', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(main(text))
print('OK~')
"""
