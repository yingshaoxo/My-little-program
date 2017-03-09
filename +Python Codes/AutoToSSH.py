import os

ip_address = '45.76.29.42'
user_name = 'root'
port = '77'
commands = ['ssh ' + user_name + '@' + ip_address + '  -p' + port]
os.system(' && '.join(commands))