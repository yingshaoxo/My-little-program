import os
import sys
import subprocess
from flask import Flask, request



def handle_message(msg):
    return (msg, '\nThis msg have ', len(msg), 'characters.')



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
        return result



tip = '''[Handle Message & Reply]GET or POST text message to http://127.0.0.1:5000/Chat/
[Run Python Codes]POST Python codes to http://127.0.0.1:5000/Python/
I'll back the result if you POST something to me.'''


def decode(data):
    try:
        codes = data.decode('utf-8')
    except:
        codes = data.decode('gb2312')
    return codes


app = Flask(__name__)

@app.route('/')
def home_page(): #http://127.0.0.1:5000
    return tip

@app.route('/Chat/', methods=['GET', 'POST'])
def reply_message():
    if request.method in ['GET', 'POST']:
        msg = decode(request.data)

        if msg == '':
            print('Nothing received.')
            return ''
        else:
            return handle_message(codes) 

@app.route('/Python/', methods=['POST'])
def run_python():
    if request.method == 'POST':
        codes = decode(request.data)

        if codes == '':
            print('Nothing received.')
            return ''
        else:
            return run_py_codes(codes)

if __name__ == '__main__':
    print(tip)
    app.run()