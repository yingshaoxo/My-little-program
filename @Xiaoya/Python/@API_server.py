from flask import Flask, request, redirect


import socket
local_host = socket.gethostbyname(socket.gethostname())
tip = '''Only receive "content_type='text; charset=utf-8'" and "Accept-Encoding='utf-8'"!!!
[Handle Message & Reply] POST text message to http://{host}:5000/Chat/
[Run Python Codes] POST Python codes to http://{host}:5000/Python/
[Search data] POST key word to http://{host}:5000/Search/'''.format(host=local_host)


def chat_reply(msg):
    from __Xiaoya__ import xiaoya
    x = xiaoya('xiaoya', 17, 'books')
    return x.reply(msg).strip('  　\n ')

def chat_send(msg):
    from __Message__ import get_message
    return get_message()

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
def home_page():
    return tip.replace('\n', '<br>')

@app.route('/Chat/', methods=['GET', 'POST'])
def chat_with_xiaoya():
    if request.method =='GET':
        return 'Now IP=' + request.remote_addr + ', you can POST a chat-message to me.'
    if request.method == 'POST':
        msg = decode(request.data)
        
        if msg == '':
            print('Nothing received.')
            return ''
        else:
            return chat_reply(msg)
        
@app.route('/Send/', methods=['GET', 'POST'])
def send_with_xiaoya():
    if request.method =='GET':
        return 'This is for server itself, other language could POST a message ask me which is needed to send directly.'
    if request.method == 'POST':
        msg = decode(request.data)
        return chat_send(msg)

@app.route('/Search/', methods=['GET', 'POST'])
def search_data():
    if request.method =='GET':
        return 'Now, you can POST search-words to me.'
    if request.method == 'POST':
        msg = decode(request.data)

        if msg == '':
            return ''
        else:
            from __Analysis__ import search
            try:
                return search(msg)
            except Exception as e:
                print(e)
                return ''

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


def split_sentence():
    from Plugins.Extensions.GetEnglish.SplitSentence import main as _split
    msg = decode(request.data) 
    return _split(msg.replace(' ', ' '))
app.add_url_rule('/Tools/split', view_func=split_sentence, methods=['POST'])

def translate_sentence():
    from Plugins.Extensions.GetEnglish.SplitSentenceAndTranslate import main as _translate
    msg = decode(request.data)
    return _translate(msg.replace(' ', ' '))
app.add_url_rule('/Tools/translate', view_func=translate_sentence, methods=['POST'])

def tools_run_python():
    msg = decode(request.data)
    return run_codes(msg)
app.add_url_rule('/Tools/python', view_func=tools_run_python, methods=['POST'])


app.register_error_handler(500, lambda e: '')  # Fail to run the codes!\nPlease check it carefully.

if __name__ == '__main__':
    print(tip)
    app.run(host='0.0.0.0')
