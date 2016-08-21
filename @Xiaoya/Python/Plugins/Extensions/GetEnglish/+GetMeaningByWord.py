from bs4 import BeautifulSoup
import requests

def get_chinese(word):
    r = requests.get('http://www.collinsdictionary.com/dictionary/english-chinese/' + word)
    soup = BeautifulSoup(r.text, 'html.parser')
    description = soup.find('ol',  attrs={"class":"sense_list level_1"}).get_text()
    description = description.replace('\n\n\n\n', '\n\n\n').replace('\n\n', '\n').replace('\n', '\n\n')
    return description

def get_English(word):
    r = requests.get('http://www.collinsdictionary.com/dictionary/english/' + word)
    soup = BeautifulSoup(r.text, 'html.parser')
    description = soup.find('span',  attrs={"class":"hom"}).get_text()
    description = segment_by_num(description)
    try:
        description = '1.' + description.split('1.')[1]
    except:
        description = description
    return description.replace(u'\xa0', u'').replace(u'\u21d2', u'-->')

def segment_by_num(text):
    for i in range(1,20):
        num = str(i) + '.'
        text = text.replace(num, '\n\n'+num)
    return text

text = 'perfect'
print(text + '\n\n' + get_English(text))
