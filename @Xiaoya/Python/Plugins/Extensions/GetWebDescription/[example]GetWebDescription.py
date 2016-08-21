#Now, I made it, get a website description.
from bs4 import BeautifulSoup
import requests

def get_web_description1(website):
    r = requests.get(website)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        title = soup.title.string
    except:
        title = ''

    try:
        description = soup.find('meta',  attrs={"name":"description"})['content']
        #soup.find_all('meta',  attrs={"name":"description"}, limit=7)[0]['content']
    except:
        description = ''
        
    if (title == '' or description == ''):
        result = title + description
    else:
        result = title + '\n\n' + description
    
    return result




import re

def get_web_description2(website):
    r = requests.get(website)
    title = re_get_first_text(r"<title>[\s\S]*?</title>", r.text)
    title = title.replace('<title>', '').replace('</title>', '')

    description = re_get_first_text(r'''<meta[^>]*name=[\"|\']description[\"|\'][^>]*content=[\"]([^\"]*)[\"][^>]*>''', r.text)
    description = description.replace(''''<meta name="description" content="''', '').replace(''''<meta name="description"  content="''', '').replace('/', '').replace('"', '').replace('>', '')

    if (title == '' or description == ''):
        result = title + description
    else:
        result = title + '\n\n' + description
    
    return result


def re_get_first_text(regular_expression, from_text):
    result_list = re.findall(regular_expression, from_text)
    if (len(result_list) != 0):
        return result_list[0]
    else:
        return ''




def get_URLs(text):
   return re_get_first_text(r'https?://\S+', text) 

    

while True:
    website = input('Input a website and press Enter, please: ')
    website = get_URLs(website)
    print('\n\n'+get_web_description1(website)+'\n\n'+'-'*17)
    print('-'*17+'\n\n'+get_web_description2(website)+'\n\n'+'-'*17)
