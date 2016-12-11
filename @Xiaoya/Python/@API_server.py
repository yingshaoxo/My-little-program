from flask import Flask, request, redirect


import socket
local_host = socket.gethostbyname(socket.gethostname())
tip = '''[Handle Message & Reply] POST text message to http://{host}:5000/Chat/
[Run Python Codes] POST Python codes to http://{host}:5000/Python/
[Search data] POST key word to http://{host}:5000/Search/'''.format(host=local_host)

def chat_room(msg):
    return ''

def chat_reply(msg):
    try:
        with open('SayingOfYingshaoxo.txt', 'a', encoding='utf-8') as f:
            f.write(msg + '\n\n——————————————\n\n')
    except:
        print('Fail to store saying.')
    from __Xiaoya__ import xiaoya
    x = xiaoya('xiaoya', 17)
    return x.reply(msg)

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
        return 'Now, you can POST chat-message to me.'
    if request.method == 'POST':
        msg = decode(request.data)

        if msg == '':
            print('Nothing received.')
            return ''
        else:
            return chat_reply(msg) 

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

app.register_error_handler(500, lambda e: '')  # Fail to run the codes!\nPlease check it carefully.

if __name__ == '__main__':
    print(tip)
    app.run(host='0.0.0.0')
