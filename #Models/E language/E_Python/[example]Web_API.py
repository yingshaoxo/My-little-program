from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Welcome to your own web server!'
    #http://127.0.0.1:5000

@app.route('/Python/', methods = ['POST', 'GET'])
def run_python():
    if request.method == 'GET':
        return 'Only support POST!'
        #http://127.0.0.1:5000/Python

    elif request.method == 'POST':
        return "Here's your codes:\n\n" +  request.data.decode('utf-8')
        #POST text to http://127.0.0.1:5000/Python/

if __name__ == '__main__':
    app.run()


