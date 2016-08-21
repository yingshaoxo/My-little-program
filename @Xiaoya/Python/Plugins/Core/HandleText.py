def OrganizeText(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　'):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　'):#right
        text = text[:-1]
    
    return text


def RemoveAllAdditionalLines(text):
    text = text.replace('\n\n', '\n')
    while (text[0:1] == '\n' and text[-1:] == '\n'):
        text = text[1:]
        text = text[:-1]
    
    return text


def SplitSentences(text):
    text = text.replace('.', '.\n')
    text = text.replace('?', '?\n')
    text = text.replace('!', '!\n')
    text = text.replace(';', ';\n')
    sentences_list = text.split('\n')

    return sentences_list


def SplitWords(text):
    text = text.replace('\n', '')
    words_list = text.split(' ')
    
    return words_list


example = '''
醉花阴
 


薄雾浓云愁永昼，瑞脑消金兽。 

佳节又重阳，玉枕纱厨，半夜凉初透。

东篱把酒黄昏后，有暗香盈袖。 

莫道不销魂，帘卷西风，人比黄花瘦。


'''

result = OrganizeText(example)
print(result)
