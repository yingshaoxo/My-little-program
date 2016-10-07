import os
import re
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
#            print(txt_files)
            if old_books == None:
                new_txt = txt_files
                old_books = {'NO': 0}
            else:
                new_txt = [i for i in txt_files if i not in old_books]
            
            for i in new_txt:
                old_books.update({i: 0})
            if 'NO' in old_books:
                del old_books['NO']

            for i in [i for i in old_books.keys() if i not in txt_files]:
                del old_books[i]
        
            setting.update({'books': old_books})
            write_setting(setting)

        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        if not os.path.exists(self.dir + 'setting.json'):
            write_setting({'books': {'NO': 0}})
        
        update_setting()

    def get_knowledge0(self):
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
                print('We only support UTF_8!')
                
            result = text.split('\n\n' + '——————————————' + '\n\n')
            if result == [text]:
                result = text.split('\n')
            result = [i for i in result if re.match(r'^\s*$', i) == None]

            return result

        def which_part():
            setting = get_setting()
            books = setting.get('books')

            import random
            book = random.choice(list(books.keys()))
            print(book)
            num = books.get(book)
            print(num)
            try:
                part = split_txt(self.dir + book)[num]
            except:
                part = 'Your reading was finished with this book.'
                os.rename(self.dir + book, self.dir + book.replace('.txt', '.bak'))
#            print(part)

            num += 1
            books.update({book: num})
            setting.update({'books': books})
            print(setting, '\n')
            write_setting(setting)

            return part

        return which_part().replace('\n', '\n\n')
    
    def get_knowledge(self):
        from Plugins.Core.HandleText import EnglishOrNot, OrganizeText
        knowledge = self.get_knowledge0()
        if EnglishOrNot(knowledge):
            from Plugins.Core.NaturalLanguageProcessing import from_ariticle_get_word
            try:
                en_words = from_ariticle_get_word(knowledge)
                if OrganizeText(en_words) != '':
                    knowledge += '\n\n' + '——————————————' + '\n\n' + en_words
            except Exception as e:
                print(e)
        return knowledge
 
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
        return k.get_knowledge()


#x = xiaoya('xiaoya', 17)
#print(x.knowledge())
