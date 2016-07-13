import sys
import os
import subprocess

EXEC = sys.executable #local pythonw.exe

def run_py_file(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        return str(result.stdout)
    else:
        return 'error'

def run_py_codes(py_codes):
    codes = str(py_codes)
    if codes.count('print(')==0 and codes.count('import ')==0:
        result = str(eval(codes))
        return result
    else:
        py_path = os.path.dirname(os.path.realpath(__file__)) + '\\codes.txt'
        with open(py_path, 'w') as out:
            out.write(codes)
        result = str(run_py_file(py_path))
        return result



from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home_page(): #http://127.0.0.1:5000
    return 'POST codes to http://127.0.0.1:5000/Python/'
    
@app.route('/Python/', methods = ['POST', 'GET'])
def run_python():
    if request.method == 'GET': #http://127.0.0.1:5000/Python
        return 'Only support POST!'

    elif request.method == 'POST': #POST codes to http://127.0.0.1:5000/Python/
        codes = request.data.decode('utf-8')
        if codes=='':
            return 'You give me nothing!'
        else:
            return run_py_codes(codes)

if __name__ == '__main__':
    app.run()
