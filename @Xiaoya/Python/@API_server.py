from flask import Flask, request, redirect


tip = '''[Handle Message & Reply] POST text message to http://127.0.0.1:5000/Chat/
[Run Python Codes] POST Python codes to http://127.0.0.1:5000/Python/
'''

def chat_room(msg):
    return ''

def chat_reply(msg):
    from __Xiaoya__ import xiaoya
    x = xiaoya('xiaoya', 17)
    return x.knowledge()

def run_codes(codes):
    from __RunPY__ import run_py_codes
    return run_py_codes(codes)

def decode(data):
    try:
        codes = data.decode('utf-8')
    except:
        codes = data.decode('gb2312')
    return codes


app = Flask(__name__)

@app.route('/')
def home_page(): #http://127.0.0.1:5000
    return tip.replace('\n', '<br>')

@app.route('/Chat/', methods=['GET', 'POST'])
def chat_with_xiaoya():
    if request.method =='GET':
        return 'Now, you can POST chat-message to me.'
    if request.method == 'POST':
        msg = decode(request.data)

        if msg == '':
            print('Nothing received.')
            return ''
        else:
            return chat_reply(msg) 

@app.route('/Python/', methods=['GET', 'POST'])
def run_python():
    if request.method == 'GET':
        return redirect("https://docs.python.org/3/library/index.html", code=302)  #"Now, you can POST codes to me."
    if request.method == 'POST':
        codes = decode(request.data)

        if codes == '':
            print('Nothing received.')
            return ''
        else:
            return run_codes(codes)

app.register_error_handler(500, lambda e: 'Fail to run the codes!\nPlease check it carefully.')

if __name__ == '__main__':
    print(tip)
    app.run(host='0.0.0.0')
