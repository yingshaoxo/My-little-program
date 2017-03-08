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
text = '''
坊市制主要表现为将住宅区（坊）和交易区（市）严格分开，并用法律和制度对交易的时间和地点进行严加控制。坊市制度将商业区和居住区分开，居住区内禁止经商。唐代后期，开始打破市坊制，也不再限制商品交易的时间。

在繁华城市不论白天
还是夜晚，集市贸易都
相当发达。唐代中期，随着农业、手工业的不
断发展，商业出现了新的繁荣局面，单靠白天的市场交换商品显然已不
能适应，于是夜市正式出现。

当时文人的诗作里出现过“夜市千灯照碧云，高楼红袖客纷纷。

水门向晚茶商闹，桥市通宵酒客行。

”
'''
print(split_sentence(text))

"""
