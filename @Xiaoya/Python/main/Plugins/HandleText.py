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
There is freedom waiting for you, On the breezes of the sky, And you ask 'What if I fall?' Oh but my darling, What if you fly?
'''

result = WordSegmentation(example)
print(result)
