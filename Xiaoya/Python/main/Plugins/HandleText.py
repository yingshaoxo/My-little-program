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


print(OrganizeText('''
　　　　　　　　　　　　　　
　　　　　　　　　　　　　
　　　　　　　　　　　　　　　　　

                   
.版本 2

.判断循环首 (取文本左边 (FinalText, 2) ＝ #换行符)
    FinalText ＝ 取文本右边 (FinalText, 取文本长度 (FinalText) － 2)
.判断循环尾 ()
.判断循环首 (取文本右边 (FinalText, 2) ＝ #换行符)
    FinalText ＝ 取文本左边 (FinalText, 取文本长度 (FinalText) － 2)
.判断循环尾 ()
　　　　　　　　　　　　　　
　　　　　　　　　　　　　
　　　　　　　　　　　　　　　　　

                                            
'''))
