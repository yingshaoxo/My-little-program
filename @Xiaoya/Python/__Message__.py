line = '\n\n' + '——————————————' + '\n\n'

def list_to_txt(_list):
    msg = ''
    for i in _list:
        msg += i + line
    msg = msg[:-len(line)]
    return msg

def update():
    with open('temp_message.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    _list = text.split(line)
    _list = [i.strip('  　\n ') for i in _list if i.strip('  　\n ') != '']
    
    with open('temp_message.txt', 'w', encoding='utf-8') as f:
        f.write('')
        
    return _list

def get_message():
    msg_list = update()
    if len(msg_list) == 0:
        return ''
    else:
        msg = list_to_txt(msg_list)
        return msg
