import time


line = '\n\n' + '——————————————' + '\n\n'

def txt_to_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    _list = text.split(line)
    _list = [i.strip('  　\n ') for i in _list if i.strip('  　\n ') != '']
    return _list

def list_to_txt(_list):
    msg = ''
    for i in _list:
        msg += i + line
    msg = msg[:-len(line)]
    return msg

def send_message(_list):
    msg = list_to_txt(_list)
    with open('..\\temp_message.txt', 'a', encoding='utf-8') as f:
        f.write(line + msg)
    return msg

path = 'Maths.txt'
hours = 7

minutes = hours * 60
all_list = txt_to_list(path)
#num = len(all_list)//minutes + 1
if len(all_list)//minutes != len(all_list)/minutes:
    num = len(all_list)//minutes + 1
else:
    num = len(all_list)//minutes

while 1:
    old_time = time.strftime("%H:%M")
    while 1:
        new_time = time.strftime("%H:%M")
        if new_time != old_time:
            old_time = new_time
            minute = old_time.split(':')[1]
            print(minute)
            send_message(all_list[:num])
            all_list = all_list[num:]
            if len(all_list) == 0:
                exit()
            break
