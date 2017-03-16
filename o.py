from flask import Flask, make_response, send_file
import socket
import os


your_host_ip = '45.63.90.169'
your_port = '5321'

def escape(text):
    if '#' in text:
        text = text.replace('#', '@@pound_sign@@')
    else:
        text = text.replace('@@pound_sign@@', '#')
    return text

def show(name):
    dir_ = [i for i in os.listdir(name) if os.path.isdir(os.path.join(name, i))==True]
    file_ = [i for i in os.listdir(name) if os.path.isfile(os.path.join(name, i))==True]
    all_ = ['<a href="http://{ip}:{port}/{path}">{name}</a>'.format(ip=your_host_ip, port=your_port, path=escape(os.path.join(name, i)), name=i) for i in dir_ + file_]
    css_ = '''
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--[if lt IE 9]><script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script> <![endif]-->
'''
    html = css_ + '<body>' + '<br>'.join(all_) + '</body>'
    return html

app = Flask(__name__)

@app.route('/')
def home_page():
    return show('.')

@app.route('/<path:name>')
def ftp_page(name):
    name = escape(name.strip(' '))
    print(name)
    if os.path.exists(name):
        if os.path.isfile(name):
            response = make_response(send_file(name)) 
            response.headers["Content-Disposition"] = "attachment; filename={};".format(name)
            return response
        else:
            return show(name)
    else:
        return "Give me the file name after URL!<br>I'll send it for you!"
    
if __name__ == '__main__':
    print('http://{}:{}'.format(your_host_ip, your_port))
    app.run(host='0.0.0.0', port=your_port)
