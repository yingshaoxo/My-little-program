import os
import re
import json


global path
path = os.path.dirname(__file__) 


class in_or_out():
    def __init__(self):
        self.dir = os.path.join(path, 'Sources')
        self.setting_file_name = 'setting.json'
        self.setting_file_path = os.path.join(self.dir, self.setting_file_name)
        
    def get_setting(self):
        with open(self.setting_file_path, 'r') as f:
            text = f.read()
        return json.loads(text)

    def write_setting(self, a_dict):
        with open(self.setting_file_path, 'w') as f:
            f.write(json.dumps(a_dict, sort_keys=True, indent=4))

    def split_txt(self, file_name):
        try:
            with open(file_name, 'r',  encoding='utf-8', errors='ignore') as f: 
                text = f.read()
        except Exception as e:
            print(e)
            print('We only support UTF_8!')
            
        result = text.split('\n\n' + '——————————————' + '\n\n')
        if result == [text]:
            result = text.split('\n')
        result = [i for i in result if re.match(r'^\s*$', i) == None]

        return result


class update(in_or_out):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = str(user_id)

        if os.path.exists(self.dir) == False:
            os.mkdir(self.dir)
        if os.path.exists(self.setting_file_path) == False:
            self.write_setting({'NO':0})

        self.update_setting()

    def update_setting(self):
        setting = self.get_setting()
        old_books = setting.get(self.user_id)

        txt_files = [i for i in os.listdir(self.dir) if '.txt' in i]

        if old_books == None:
            new_txt = txt_files
            old_books = {'NO': 0}
        else:
            new_txt = [i for i in txt_files if i not in old_books]

        for i in new_txt:
            old_books.update({i: 0})

        if 'NO' in setting:
            del setting['NO']

        for i in [i for i in old_books.keys() if i not in txt_files]:
            del old_books[i]

        setting.update({self.user_id: old_books})
        self.write_setting(setting)


class knowledge(update):
    def __init__(self, user_id):
        super().__init__(user_id)

    def get_random_one(self):
        setting = self.get_setting()
        books = setting.get(self.user_id)

        if books == {}:
            return ''

        import random
        book_name = random.choice(list(books.keys()))
        book_path = os.path.join(self.dir, book_name)

        num = books.get(book_name)
        print(book_name,num)

        try:
            one = self.split_txt(book_path)[num]
        except:
            one = 'You finished your reading with ' + book_name + '.'
            try:
                os.rename(book_path, book_path.replace('.txt', '.bak'))
            except:
                os.remove(book_path)

        num += 1
        books.update({book_name: num})
        setting.update({self.user_id: books})
        self.write_setting(setting)
        
        return one.strip('  　\n ')



class skill():
    def __init__(self, user_id):
    	self.user_id = user_id

    def knowledge(self):
        k = knowledge(self.user_id)
        text = k.get_random_one()
        return text.replace('\n', '\n'*2)

    def baike(self, key_word):
        from Plugins.Extensions.GetBaike.Baike import main as baike
        return baike(key_word)
        
    def run_python(self, codes):
        from __RunPY__ import run_py_codes
        return run_py_codes(codes)    


class xiaoya(skill):
    '''A real xiaoya class'''
    def __init__(self, name, age, user_id):
        self.name = name
        self.age = age
        super().__init__(user_id)
        print(self.about())

    def about(self):
        return ("My name is {name}.\nAnd I'm {age} years old now.\n".format(name=self.name, age=self.age))

    def reply(self, msg):
        if msg[:6] == '#codes':
            return self.run_python(msg)
        elif msg[:6] == '#baike':
            msg = msg.replace('#baike', '').strip('  　\n ')
            return self.baike(msg)
        else:
            return self.knowledge()




#x = xiaoya('xiaoya', 17, 'test')
#print(x.reply('#codes\nimport os\nprint(os.system("ls"))'))
#print(x.reply('#baike good'))
