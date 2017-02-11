import os


path = 'Coding/temp.py'

def read():
    with open(path, 'r+t', encoding='utf-8') as f:
        result = f.read()
    return result
    
def start(text):
    os.remove(path)
    with open(path, 'w+t', encoding='utf-8') as f:
        f.write('#coding start...\n\n' + text)
    return read()

def coding(text):
    with open(path, 'a+t', encoding='utf-8') as f:
        f.write('\n' + text)
    return read()

def end(text):
    from __RunPY__ import run_py_codes
    with open(path, 'a+t', encoding='utf-8') as f:
        f.write(text)
    all_codes = read()
    return all_codes +'\n\n#coding end...'  + '\n\n——————————————\n\n' + run_py_codes(all_codes)
        
def save(text):
    import pprint
    with open('Coding/' + text, 'w+t', encoding='utf-8') as f:
        f.write(read())
    return pprint.pformat(os.listdir('Coding'))

def look(text):
    with open('Coding/' + text, 'r+t', encoding='utf-8') as f:
        result = f.read()
    return result
