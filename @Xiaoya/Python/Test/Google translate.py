import requests
import json


#https://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&hl=zh-CN&dt=at&ie=UTF-8&oe=UTF-8&q=sure
text = '''Right now your dad and I have been married for about two years'''
r = requests.post('https://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&hl=zh-CN&dt=at&ie=UTF-8&oe=UTF-8&q='\
                              + text)
result = r.text
with open('ddd.txt', 'w', encoding='utf-8') as f:
    f.write(result)

'''
[,,"en",,,[["Right now your dad and I have been married for about two years, living on Ellis Avenue;",,[["现在你的爸爸和我结婚了大约两年，住在埃利斯大道;",0,true,false],["现在你爸爸和我已经结婚两年左右，住在埃利斯大道;",0,true,false]],[[0,87]],"Right now your dad and I have been married for about two years, living on Ellis Avenue;",0,0],["when we move out you'll still be too young to remember the house, but we'll show you pictures of it, tell you stories about it.",,[["当我们搬出去，你仍然会太年轻，不记得房子，但我们会给你的照片，告诉你关于它的故事。",0,true,false],["当我们走出你仍然太年轻，还记得房子，但我们会告诉你它的照片，告诉你它的故事。",0,true,false]],[[0,127]],"when we move out you'll still be too young to remember the house, but we'll show you pictures of it, tell you stories about it.",0,0],["I'd love to tell you the story of this evening, the night you're conceived, but the right time to do that would be when you're ready to have children of your own, and we'll never get that chance.",,[["我想告诉你这个晚上的故事，你的构想的夜晚，但正确的时间做到这一点，当你准备好你自己的孩子，我们永远不会得到这个机会。",0,true,false],["我很想告诉你，今天晚上的故事，你所设想的晚，但要做到这一点，当你准备拥有自己的孩子会是合适的时间，我们将永远不会得到这样的机会。",0,true,false]],[[0,195]],"I'd love to tell you the story of this evening, the night you're conceived, but the right time to do that would be when you're ready to have children of your own, and we'll never get that chance.",0,0]]]
'''
