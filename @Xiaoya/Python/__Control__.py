import os


path = 'Coding/temp.py'

def read():
    with open(path, 'r+t', encoding='utf-8') as f:
        result = f.read()
    return result.replace('\n\n', '\n')
    
def start(text):
    os.remove(path)
    with open(path, 'w+t', encoding='utf-8') as f:
        f.write('#Programming start...\n\n' + text)
    return read()

def coding(text):
    with open(path, 'a+t', encoding='utf-8') as f:
        f.write('\n\n# Go on programming\n\n' + text)
    return read()

def end(text):
    from __RunPY__ import run_py_codes
    with open(path, 'a+t', encoding='utf-8') as f:
        f.write(text)
    all_codes = read()
    return '#codes\n' + all_codes +'\n\n#Programming end...\n'  + '\"\"\"\n\n——————————————\n\n' + run_py_codes(all_codes) + '\n\n——————————————\n\n\"\"\"'
        
def save(text):
    import pprint
    with open('Coding/' + text, 'w+t', encoding='utf-8') as f:
        f.write(read())
    return pprint.pformat(os.listdir('Coding'))

def look(text):
    from __RunPY__ import run_py_codes
    with open('Coding/' + text, 'r+t', encoding='utf-8') as f:
        all_codes = f.read()
    return '#codes\n' +all_codes  + '\n'  + '\"\"\"\n\n——————————————\n\n' + run_py_codes(all_codes) + '\n\n——————————————\n\n\"\"\"'

def run(text):
    from __RunPY__ import run_py_codes
    old = '''
import os
os.system('{codes}')
'''
    new = old.format(codes=text)
    print(new)
    return run_py_codes(new)  
