class a:
    def __init__(self):
        def b(c):
            return c*2
        def d(c):
            return c*2
        print(d(b(1)))

s = a()
