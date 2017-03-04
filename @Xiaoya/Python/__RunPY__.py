import os
import sys
import subprocess


EXEC = sys.executable #local pythonw.exe

def run_py_file(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    return str(result.stdout)

def run_py_codes(py_codes):
    codes = str(py_codes)
    if codes.count('print') == 0 and codes.count('import') == 0:
        try:
            result = str(eval(codes))
        except Exception as e:
            result = str(e)
        return result
    else:
        py_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'codes.txt')
        code_bytes = codes.encode('utf-8', 'ignore')
        open(py_path, 'wb').write(code_bytes)
        result = str(run_py_file(py_path))
        os.remove(py_path)
        return result
