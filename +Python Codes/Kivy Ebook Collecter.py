from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import os


def find_all_books(base_folder):
    '''return all Ebook path'''
    file_list = []
    for root, dirs, files in os.walk(base_folder, topdown=False): # find all files
        for name in files:
            path = os.path.join(root, name)
            #print(path)
            if path.split('.')[-1] in ['pdf', 'epub', 'mobi']:
                file_list.append(path)
        for name in dirs:
            pass
    if len(file_list) == 0: # if no file frond, show the current folder path
        file_list.append(base_folder)
    return file_list


Builder.load_string('''
<RootWidget>:
#This is the root widget's kv definition
    Screen:
        name: 'Home'
        
        GridLayout:
            cols: 1
            Button:
                text: 'Show All Ebooks'
                on_release: root.current = 'Show'
                size_hint_y: 0.7
                pos_hint: {"left": 0, "top":1}

            Button:
                text: 'Collect All Ebooks to One Folder'
                on_release: root.collect()
                size_hint_y: 0.3
                pos_hint: {"left": 0, "top":0.5}
            
    Screen:
        name: 'Show'
        
        ListView:
            item_strings: root.all_books_name
            size_hint: 1, 0.8
            pos_hint: {"left": 0, "top":1}
            
        Button:
            text: 'Back Home'
            on_release: root.current = 'Home'
            size_hint: 1, 0.2
            pos_hint: {"bottom":1}
''')


class RootWidget(ScreenManager):
    '''This the class representing your root widget.
       By default it is inherited from ScreenManager,
       you can use any other layout/widget depending on your usage.
    '''
    def __init__(self, **kwargs):
        self.base_folder =os.path.dirname(os.path.abspath('.'))
        self.all_books_path = find_all_books(self.base_folder)
        self.all_books_name = [os.path.basename(name) for name in self.all_books_path]
        super(RootWidget, self).__init__(**kwargs)
        
        self.home_screen = self.get_screen('Home')

    def collect(self):
        '''collect all books to one folder'''
        if self.all_books_path[0] != self.base_folder: # detect if no books found
            goal_folder = os.path.join(self.base_folder, 'Books')
            if not os.path.exists(goal_folder): # if no goal_folder exists, creat a new one
                os.mkdir(goal_folder)
            for path in self.all_books_path: # move file
                goal_path = os.path.join(goal_folder, os.path.basename(path))
                os.rename(path, goal_path)
            Popup(title='Tip', content=Label(text='All Ebooks collected in \n'+goal_folder), size_hint=(None, None) ,size=(350, 350)).open()
        

class MainApp(App):
    '''This is the main class of your app.
       Define any app wide entities here.
       This class can be accessed anywhere inside the kivy app as,
       in python::

         app = App.get_running_app()
         print (app.title)

       in kv language::

         on_release: print(app.title)
       Name of the .kv file that is auto-loaded is derived from the name
       of this class::

         MainApp = main.kv
         MainClass = mainclass.kv

       The App part is auto removed and the whole name is lowercased.
    '''

    def build(self):
        '''Your app will be build from here.
           Return your widget here.
        '''
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
