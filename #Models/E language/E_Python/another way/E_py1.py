import subprocess

EXEC = '*executable*'

def py_run(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'error'

result = py_run('*py_path*')
try:
    f = open('*result.txt*', 'w')
    f.write(result)
    f.close()
except:
    print('error')
