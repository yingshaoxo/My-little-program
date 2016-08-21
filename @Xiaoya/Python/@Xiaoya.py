class xiaoya:
    '''A real xiaoya class'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.about())

    def about(self):
        return ("My name is {name}.\nAnd I'm {age} years old now.".format(name=self.name, age=self.age))

    def reply(self, msg):
    	return msg
