def output(text):
    print(text)

class xiaoya:
    '''A real xiaoya class'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        output("My name is {name}.\nAnd I'm {age} years old now.".format(name=self.name, age=self.age))


xy = xiaoya('xiaoya', '17')
xy.about()
