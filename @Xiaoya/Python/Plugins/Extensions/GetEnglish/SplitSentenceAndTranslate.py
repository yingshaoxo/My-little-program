import requests

def OrganizeText(text):
    while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　' or text[0:1] == ' '):#left
        text = text[1:]
    while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　' or text[-1:] == ' '):#right
        text = text[:-1]
        
    return text

def SplitSentences(text):
    text = OrganizeText(text)
    
    text = text.replace('. ', '.\n')
    text = text.replace('? ', '?\n')
    text = text.replace('! ', '!\n')
    text = text.replace('; ', ';\n')
    
    if text.count('\n')<5:
        text = text.replace('. ', '.\n')
        text = text.replace('? ', '?\n')
        text = text.replace('! ', '!\n')
        text = text.replace('; ', ';\n')
    
    text = OrganizeText(text)
    sentences_list = text.split('\n')
    all_sentences = ''
    for num, each in enumerate(sentences_list, start=0):
        one_sentence = OrganizeText(each)
        sentences_list[num] = one_sentence
        all_sentences += one_sentence
        
    return sentences_list


def youdao_translate(text):
    r = requests.get('http://fanyi.youdao.com/openapi.do?keyfrom=yingshaoxo&key=61881981&type=data&doctype=text&version=1.0&q=' \
     + text)
    translation = r.text.split('result=')[1][:-2]
    return text + '\n' + translation

    
def main(msg):
    text = msg
    sentence_lists = SplitSentences(text)
    result = ''
    for num, sentence in enumerate(sentence_lists, start=0):
        try:
            result += youdao_translate(sentence)
        except:
            result += sentence
        if num != len(sentence_lists)-1:
            result += '\n' * 2
        else:
            result += '\n' * 2
    return result

#print(youdao_translate('yes'))
