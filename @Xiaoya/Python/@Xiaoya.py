import os
import json


global path
path = os.path.dirname(__file__) + '\\'


class knowledge:
    '''Get knowledge from txt file.'''
    def __init__(self):
        sources_dir = path + 'Sources\\'
        
        if not os.path.exists(sources_dir):
            os.mkdir(sources_dir)
            with open(sources_dir + 'setting.json', 'w') as f:
                f.write(json.dumps({'books': []}, sort_keys=True, indent=4))

        with open(sources_dir + 'setting.json', 'r') as f:
                text = f.read()
        setting = json.loads(text)
        old_books = setting.get('books')

        txt_files = [i for i in os.listdir(sources_dir) if '.txt' in i]
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
        with open(sources_dir + 'setting.json', 'w') as f:
            f.write(json.dumps(setting, sort_keys=True, indent=4))        
    
    def get_setting(self):
        sources_dir = path + 'Sources\\'
        with open(sources_dir + 'setting.json', 'r') as f:
                text = f.read()
        setting = json.loads(text)
        return setting


class xiaoya:
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
        print(k.get_files_in_dir())


x = xiaoya('xiaoya', 17)
x.knowledge()
