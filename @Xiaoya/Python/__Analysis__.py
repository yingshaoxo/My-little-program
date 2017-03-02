# encoding=utf-8
import os
from difflib import SequenceMatcher 
from difflib import get_close_matches


global path
path = os.path.dirname(__file__) + '\\Date\\' 
if os.path.exists(path) == False:
    os.mkdir(path)

def similar(a, b): 
    return SequenceMatcher(None, a, b).ratio()
    #.ratio()
    #.quick_ratio()
    #.real_quick_ratio()
    
def match(word, a_list):
    result = get_close_matches(word, a_list, 1)
    if len(result) == 0:
        return ''
    else:
        return result

           
def max_close(word, a_list):
    max = [0,0.0]
    #min = [0,0.0]
    if len(a_list) == 0:
        return ''
    for num, text in enumerate(a_list, start=0):
        similarity = similar(word, a_list[num])
        #print(similarity,'\n')
        if similarity > 0:
            if similarity > max[1]:
                max[1] = similarity
                max[0] = num
            #elif similarity < min[1]:
                #min[1] = similarity
                #min[0] = num
    
    #print('max: {}\n'.format(max[1]))
    #print(max[0])
    #print(a_list[max[0]])
    return a_list[max[0]]
    
    #if min[1] > 0:
        #print('\n\n', '-'*10, '\n\n')
        #print('min: {}\n\n'.format(min[1]))
        #print(min[0])
        #print(a_list[min[0]])


def split_txt(dirname):
    import re
    try:
        with open(dirname, 'r',  encoding='utf-8', errors='replace') as f:
            text = f.read()
        result = text.split('\n\n' + '——————————————' + '\n\n')	
        if result == [text]:
            result = text.split('\n')
        result = [i for i in result if re.match(r'^\s*$', i) == None]
    except Exception as e:
        print(e)
        print('We only support UTF_8!')
        result = []

    return result

def list_to_split_text(_list, num_of_line):
    text = ''
    for num, i in enumerate(_list, start=1):
        if num % num_of_line != 0:
             text += i.replace('\n', '\n\n') + '\n'
        else:
              text += i.replace('\n', '\n\n') + '\n\n——————————————\n\n'
    return text[:-16]

def search(word):
    txt_files = [path + i for i in os.listdir(path) if '.txt' in i]
    result_list = []
    for i in txt_files:
        a_list = split_txt(i)
        result_list.append(max_close(word, a_list))
        
    return list_to_split_text(result_list, 1)


def similar_myway(seg_list, b):
    '''
    num = 0
    for word in seg_list:
        num += b.count(word)
    return num
    '''
    num = 0
    for word in seg_list:
        num += similar(word, b)
    return num
    

def seg_close(text, a_list):
    import jieba
    #seg_list = list(jieba.cut_for_search(text))
    seg_list = list(jieba.cut(text))
    max = [0,0.0]
    if len(a_list) == 0:
        return ''
    for num, text in enumerate(a_list, start=0):
        similarity = similar_myway(seg_list, a_list[num])
        #print(similarity,'\n')
        if similarity > 0:
            if similarity > max[1]:
                max[1] = similarity
                max[0] = num
    if max[1] == 0:
        return ''
    else:
        return a_list[max[0]]    

def search2(text):
    txt_files = [path + i for i in os.listdir(path) if '.txt' in i]
    result_list = []
    for i in txt_files:
        a_list = split_txt(i)
        result_list.append(seg_close(text, a_list))
        
    return list_to_split_text(result_list, 1)

'''
while True:
    word = input('What you want to search?   ')
    print(search(word))
'''
