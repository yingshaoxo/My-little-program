#Now, I made it, get a website description.

import requests
import re


def get_URLs(text):
   return re_get_first_text(r'https?://\S+', text) 


def get_web_description(website):
    r = requests.get(website)
    title = re_get_first_text("<title>[\s\S]*?</title>", r.text)
    title = title.replace('<title>', '').replace('</title>', '')

    description = re_get_first_text('''<meta[^>]*name=[\"|\']description[\"|\'][^>]*content=[\"]([^\"]*)[\"][^>]*>''', r.text)
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
    
def from_text_get_website_description(text):
   website = get_URLs(text)
   return get_web_description(website)
   

text = '''#*527*your text*527*'''
try:
   print(from_text_get_website_description(text))
except:
   print('')
