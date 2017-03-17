import re


class in_or_out():
    def read_txt(self, txt_dir):
        with open(txt_dir, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    
    def write_txt(self, txt_dir, text):
        with open(txt_dir, 'w', encoding='utf-8') as f:
            f.write(text)
            
class simple():
    def pure(self, text):
        return text.strip('  　\n ')

class split(simple):
    def __init__(self, split_string='\n\n' + '——————————————' + '\n\n'):
        self.split_string = split_string
        
    def text_to_list(self, text):
        result = text.split(split_string)
        if result == [text]:
            result = text.split('\n')
        result = [self.pure(i) for i in result if re.match(r'^\s*$', i) == None]   

    def list_to_text(list_):
        return split_string.join(list_)

class text_tool(in_or_out, split):
    def language_check(self, text):
        if re.match(r'[\u4e00-\u9fa5]', text) is None:
            return 'English'
        else:
            return 'Chinese'

    def text_to_sentences(self, text):
        def handle(obj):
            text = self.pure(obj.group(0))
            return text + '\n'*2
        text = re.sub(r'((.*?)(?<!B|A)([！？。]))', handle, text)
        a_list = text.split('\n')
        a_list = [self.pure(i) for i in a_list if re.match(r'^\s*$', i) == None]
        text = '\n'.join(a_list)
        return self.pure(text)
"""
text = '''
hello?kkkkk
'''
tool = text_tool()
print(tool.text_to_sentences(text))
"""
