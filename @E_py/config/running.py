import subprocess

EXEC = 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35-32\\python.exe'

def py_run(py_path):
    result = subprocess.run([EXEC, py_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return 'error'

result = py_run('C:\\Users\\Administrator\\Desktop\\codes\\E_py\\config\\codes.py')
try:
    f = open('C:\\Users\\Administrator\\Desktop\\codes\\E_py\\config\\result.txt', 'w')
    f.write(result)
    f.close()
except:
    print('error')