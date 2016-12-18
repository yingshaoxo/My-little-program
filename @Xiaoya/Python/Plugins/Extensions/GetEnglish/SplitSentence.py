import re


def list_to_text(_list, num_of_line):
    text = ''
    for num, i in enumerate(_list, start=1):
        if num % num_of_line != 0:
            text += i + '\n'
        else:
            text += i + '\n\n'
    return text

def OT(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　'):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　'):#right
        text = text[:-1]
    return text

def handle(obj):
    text = obj.group(0)
    text = OT(text)
    return text + '\n'*2
    
def split_sentence(text):
    text = re.sub(r'((.*?)(?<!B|A)([!?.] ) ?)', handle, text)
    a_list = text.split('\n')
    a_list = [OT(i) for i in a_list if re.match(r'^\s*$', i) == None]
 
    text = list_to_text(a_list, 1)
    return text
