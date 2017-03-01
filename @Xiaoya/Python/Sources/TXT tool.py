import re

class TXT_tool():
    def read_txt(self, txt_dir):
        with open(txt_dir, 'r', encoding='utf-8') as f:
            text = f.read()
        return text

    def write_txt(self, txt_dir, text):
        with open(txt_dir, 'w', encoding='utf-8') as f:
            f.write(text)

    def split_txt_by_special_words(self, txt_dir):
        text = self.read_txt(txt_dir)
        all_lines = [i for i in text.split('\n\n——————————————\n\n') if re.match(r'^\s*$', i) == None]
        return all_lines

    def split_txt_by_line(self, txt_dir):
        text = self.read_txt(txt_dir)
        all_lines = [i for i in text.split('\n') if re.match(r'^\s*$', i) == None]
        return all_lines

    def list_to_split_text(self, _list, num_of_line):
        text = ''
        for num, i in enumerate(_list, start=1):
            if num % num_of_line != 0:
                text += i + '\n'
            else:
                text += i + '\n\n——————————————\n\n'
        return text

tool = TXT_tool()
#print(tool.list_to_split_text(['ddddd', 'gggggggg', 'wwwwwww', 'bbbbb', 'cccc'], 2))
_list = tool.split_txt_by_line('人生.bak')
#_list = list(set(_list))
text = tool.list_to_split_text(_list, 7)
tool.write_txt('人生7.txt', text)
print('ok')
