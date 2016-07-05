from bottle import route, run

@route('/')
def home():
    return "It isn't fancy, but it's my homepage"

run(host='localhost', port=9999)

