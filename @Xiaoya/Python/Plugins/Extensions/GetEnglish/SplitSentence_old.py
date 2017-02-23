def OrganizeText(text):
   while (text[0:1] == '\n' or text[0:1] == ' ' or text[0:1] == '　' or text[0:1] == ' '):#left
       text = text[1:]
   while (text[-1:] == '\n' or text[-1:] == ' ' or text[-1:] == '　' or text[-1:] == ' '):#right
       text = text[:-1]
   
   return text


def SplitSentences(text):
   text = OrganizeText(text)
   
   text = text.replace('. ', '.\n')
   text = text.replace('? ', '?\n')
   text = text.replace('! ', '!\n')
   text = text.replace('; ', ';\n')
   
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
       '''if num != len(sentences_list)-1:
           all_sentences += '\n\n'
   sentences_list.append(all_sentences)'''
   
   return sentences_list


def ListToTextHelper(text):
   sentence_lists = SplitSentences(text)
   result = ''
   for num, sentence in enumerate(sentence_lists, start=0):
       result += sentence
       if num != len(sentence_lists)-1:
           #result += '\n\n——————————————\n\n'
           result += '\n' * 2
       else:
           #result += '\n\n——————————————\n\n'
           #result += '\n\n——————————————\n\n'
           result += '\n' * 2
   return result


def main(text):
   return ListToTextHelper(text)