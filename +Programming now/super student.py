from bs4 import BeautifulSoup
#import requests
import re

title = '-小说园-小说阅读网,免费小说阅读网'
body = ''

#r = requests.get('http://www.booksrc.net/book/1000097825/1.html', headers={'Accept-Language':'zh-CN'})
with open('page.html', 'rt') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.title.string.replace(title, '')


print(re.findall(r"""(<!--adend-->)(.*)(<!--gbkstart-->)""", html))
