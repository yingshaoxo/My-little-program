from bs4 import BeautifulSoup
import requests
import json
import re


def BaiduBaike(key_word):
    url = 'http://baike.baidu.com/client/search?app=1&uid=863798020288531&cuid=491A1DBA0DDCE44231934FD168AE36A2|135882020897368&ver=2.2.2&word='
    r = requests.get(url+key_word)
    result = r.text

    try:
        true_id = json.loads(result)['lemmaId']
    except:
        search_word = json.loads(result)['queryString']
        r = requests.get('http://baike.baidu.com/client/searchresult/?' + search_word)
        result = r.text
        try:
            true_id = json.loads(result)['searchResult'][0]['lemmaId']
        except:
            return ''

    r = requests.get('http://baike.baidu.com/client/view/'+str(true_id)+'.htm')
    r.encoding = 'url'
    result = r.text

    soup = BeautifulSoup(result, 'html.parser')
    result = soup.find('div', attrs={'class':'summary'}).get_text()

    return result

def main(key_word):
    return BaiduBaike(key_word)

'''
key_word = '淤积泥沙'
print(BaiduBaike(key_word))
'''
