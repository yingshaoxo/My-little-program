


class TXT_tool():
    def split_txt_by_line(self, txt_dir):
        with open(txt_dir, 'r', encoding='utf-8') as f:
            text = f.read()
        all_lines = [i for i in text.split('\n') if i != '']
        return all_lines

    def list_to_split_text(self, _list, num_of_line):
        text = ''
        for num, i in enumerate(_list, start=1):
            if num % num_of_line != 0:
                text += i + '\n'
            else:
                text += i + '\n\n——————————————\n\n'
        return text

    def write_txt(self, txt_dir, text):
        with open(txt_dir, 'w', encoding='utf-8') as f:
            f.write(text)


tool = TXT_tool()
#print(tool.list_to_split_text(['ddddd', 'gggggggg', 'wwwwwww', 'bbbbb', 'cccc'], 2))
_list = tool.split_txt_by_line('怪诞行为学2.txt')
text = tool.list_to_split_text(_list, 7)
tool.write_txt('[7]怪诞行为学2.txt', text)
