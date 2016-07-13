import sys
import subprocess

EXEC = sys.executable #local pythonw.exe

def py_run(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'error'

print(py_run("C:\\Users\\Administrator\\Desktop\\codes\\Programming\\TRY\\E_py\\hello.py"))

'''
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')


def py_run2(py_path):
    r = dict()
    try:
        print('Executing: %s | %s ...' % (EXEC, py_path))
        r['output'] = decode(subprocess.check_output([EXEC, py_path], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        r = dict(error='Exception', output=decode(e.output))
    except subprocess.TimeoutExpired as e:
        r = dict(error='Timeout', output='执行超时')
    except subprocess.CalledProcessError as e:
        r = dict(error='Error', output='执行错误')
    print('Execute done.\n')
    return [r['output'].encode('utf-8')]
'''
'''
with open('C:\\Users\\Administrator\\Desktop\\codes\\Programming\\TRY\\hello.py', 'r') as f:
    c = compile(f.read(), '__main__', 'exec')
print(type(c))
exec(c)
'''
