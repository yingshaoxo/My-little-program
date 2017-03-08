import re


def handle_break(obj):
    text = obj.group(0)
    if re.match(r'^\s+$', text)==None:
        return re.sub(r'\s*', '', text)
    else:
        return text
    
def fix_break(text):
    text = re.sub(r'[^。！？…；：”"》】]\s+', handle_break, text)
    return text


def list_to_text(_list, num_of_line):
    text = ''
    for num, i in enumerate(_list, start=1):
        if num % num_of_line != 0:
            text += i + '\n'
        else:
            text += i + '\n\n'
    return text

def handle(obj):
    text = obj.group(0)
    text = text.strip('  　\n ')
    return text + '\n'*2

def handle_no_space(obj):
    text = obj.group(0)
    return re.sub(r'\s*', '', text)

def split_sentence(text):
    text = fix_break(text)
    text = re.sub(r'((.*?)(?<!B|A)([！？。]))', handle, text)
    
    text = re.sub(r'“(\\.|[^“”])*”', handle_no_space, text)
    text = re.sub(r'：(\\.|[^：“])*“', handle_no_space, text)
    
    a_list = text.split('\n')
    a_list = [i.strip('  　\n ') for i in a_list if re.match(r'^\s*$', i) == None]
 
    text = list_to_text(a_list, 1)
    return text.strip('  　\n ')

def main(text):
    return split_sentence(text)


"""
with open('123.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = main(text)

with open('456.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('ok')
"""
