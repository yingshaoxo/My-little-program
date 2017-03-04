import requests
import os


def download(url, name):
    try:
        r = requests.get(url)
        with open(name, "wb") as code:
            code.write(r.content)
        return True
    except Exception as e:
        print(e)
        return False


_id = 'mbzv'
num = 39
path = 'Six2'
url = 'http://book.yunzhan365.com/xzzp/' + _id + '/files/mobile/'


if os.path.exists(path) == False:
    os.mkdir(path)

from_num = 1
for i in range(from_num, num+1):
    name = str(i) +'.jpg'
    url_now = url + name
    try:
        download(url_now, path + '/' + name)
    except:
        print(Error!!!)
        print(i)
        input()
    print(name)

