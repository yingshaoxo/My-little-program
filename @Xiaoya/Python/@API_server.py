import os
import sys
import subprocess
from flask import Flask, request, redirect



def handle_message(msg):
    from __Xiaoya__ import xiaoya
    x = xiaoya('xiaoya', 17)
    return x.knowledge()



EXEC = sys.executable #local pythonw.exe

def run_py_file(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return str(result.stdout)

def run_py_codes(py_codes):
    codes = str(py_codes)
    if codes.count('print') == 0 and codes.count('import ') == 0:
        try:
            result = str(eval(codes))
        except Exception as e:
            result = str(e)
        return result
    else:
        py_path = os.path.dirname(os.path.realpath(__file__)) + '\\codes.txt'
        code_bytes = codes.encode('utf-8', 'ignore')
        open(py_path, 'wb').write(code_bytes)
        result = str(run_py_file(py_path))
        os.remove(py_path)
        return result



tip = '''[Handle Message & Reply] POST text message to http://127.0.0.1:5000/Chat/
[Run Python Codes] POST Python codes to http://127.0.0.1:5000/Python/
'''


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
def reply_message():
    if request.method =='GET':
        return 'Now, you can POST chat-message to me.'
    if request.method == 'POST':
        msg = decode(request.data)

        if msg == '':
            print('Nothing received.')
            return ''
        else:
            return handle_message(msg) 

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
            return run_py_codes(codes)

app.register_error_handler(500, lambda e: 'Fail to run the codes!\nPlease check it carefully.')

if __name__ == '__main__':
    print(tip)
    app.run(host='0.0.0.0')
