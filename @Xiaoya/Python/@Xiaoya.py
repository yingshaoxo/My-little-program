import os
import json


global path
path = os.path.dirname(__file__) + '\\'


class knowledge():
    '''Get knowledge from txt file.'''
    def __init__(self):
        self.dir = path + 'Sources\\'

        def get_setting():
            with open(self.dir + 'setting.json', 'r') as f:
                text = f.read()
            return json.loads(text)
        
        def write_setting(a_dict):
            with open(self.dir + 'setting.json', 'w') as f:
                f.write(json.dumps(a_dict, sort_keys=True, indent=4))

        def update_setting():
            setting = get_setting()
            old_books = setting.get('books')

            txt_files = [i for i in os.listdir(self.dir) if '.txt' in i]
            print(txt_files)
            if old_books == None:
                new_txt = txt_files
                old_books = {'NO': 0}
            else:
                new_txt = [i for i in txt_files if i not in old_books]
            
            for i in new_txt:
                old_books.update({i: 0})
            if 'NO' in old_books:
                del old_books['NO']
        
            setting.update({'books': old_books})
            write_setting(setting)

        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        if not os.path.exists(self.dir + 'setting.json'):
            write_setting({'books': {'NO': 0}})
        
        update_setting()

    def get_knowledge(self):
        self.dir = path + 'Sources\\'

        def get_setting():
            with open(self.dir + 'setting.json', 'r') as f:
                text = f.read()
            return json.loads(text)
        
        def write_setting(a_dict):
            with open(self.dir + 'setting.json', 'w') as f:
                f.write(json.dumps(a_dict, sort_keys=True, indent=4))

        def split_txt(dirname):
            try:
                with open(dirname, 'r',  encoding='utf-8', errors='replace') as f:
                    text = f.read()
            except Exception as e:
                print(e)
                
            try:
                return text.split('\n\n' + '——————————————' + '\n\n')
            except Exception as e:
                print(e)
                return text.split('\n')

        def which_part():
            setting = get_setting()
            books = setting.get('books')

            import random
            book = random.choice(list(books.keys()))
            print(book)
            num = books.get(book)
            print(num)
            part = split_txt(self.dir + book)[num]
            print(part)

            num += 1
            books.update({book: num})
            setting.update({'books': books})
            print(setting)
            write_setting(setting)

        return which_part()

 
class xiaoya():
    '''A real xiaoya class'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.about())

    def about(self):
        return ("My name is {name}.\nAnd I'm {age} years old now.\n".format(name=self.name, age=self.age))

    def reply(self, msg):
        return msg

    def knowledge(self):
        k = knowledge()
        print(k.get_knowledge())


x = xiaoya('xiaoya', 17)
x.knowledge()
