with open('result.txt', 'r', encoding='utf-8') as f:
    text = f.read()

split_words = '''zone
n. 地带；地区；联防
vi. 分成区
vt. 使分成地带；环绕
n. (Zone)人名；(塞)佐内


Then we add the picture to the "trash" zone.
然后，把这个照片添加到 “垃圾” 区中。

They circumnavigated the danger zone and speeded along.
他们绕过危险地带疾驶而去。

There are ways to move it, but you must create your volumes in the same availability zone as your server.
有办法可以移动它们，但是您必须在同一可用性区域中创建您的卷作为服务器。

——————————————
'''

result = text.split(split_words)[1]

with open('ok.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print('ok')
