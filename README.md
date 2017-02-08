# My little program

Based on Easy Programming Language or Python, some programs made by myself.

```python
import requests


url = 'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'

try:
    r = requests.get(url)
    hosts = r.text
except:
    print("I can't get the hosts. Can you give me another hosts url?")

try:
    with open('/etc/hosts', 'w') as f:
        f.write(hosts)
except:
    print("I can't write the hosts to your computer. Can you give me the super permission, like sudo?")

print('Fine, now.')
```
