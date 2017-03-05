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
    text = re.sub(r'((.*?)(?<!B|A)([！？。]))', handle, text)
    a_list = text.split('\n')
    a_list = [OT(i) for i in a_list if re.match(r'^\s*$', i) == None]
 
    text = list_to_text(a_list, 1)
    return text.strip('  　\n ')

def main(text):
    return split_sentence(text)

'''
text = '实施“985工程”，是中国共产党和中华人民共和国国务院在世纪之交作出的重大决策。1998年5月4日，时任国家主席江泽民在庆祝北京大学建校100周年大会上代表中国共产党和中华人民共和国中央人民政府向全社会宣告：“为了实现现代化，我国要有若干所具有世界先进水平的一流大学。”1999年，国务院批转教育部《面向21世纪教育振兴行动计划》，“985工程”正式启动建设。“985工程”一期建设率先在北京大学和清华大学开始实施。2004年，根据《2003—2007年教育振兴行动计划》，教育部、财政部印发《教育部、财政部关于继续实施“985工程”建设项目的意见》，启动了“985工程”二期建设。2010年，根据《国家中长期教育改革和发展规划纲要（2010—2020年）》，教育部、财政部印发《教育部、财政部关于加快推进世界一流大学和高水平大学建设的意见》，新一轮“985工程”建设开始实施。“985工程”建设任务为机制创新、队伍建设、平台建设、条件支撑和国际交流与合作等五个方面；采取国家、共建部门（有关主管部委或地方政府）和高等学校三级管理方式，以高等学校自我管理为主；建设实行项目管理和绩效考评。2016年06月23日，教育部官网发布文件，宣布382份规范性文件失效，包含《关于继续实施“985工程”建设项目的意见》等“985”“211”工程以及重点、优势学科建设的相关文件。 '
print(split_sentence(text))
'''
