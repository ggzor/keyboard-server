import sys
import os
from flask import Flask, request, send_from_directory
from pynput.keyboard import Controller

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:file>')
def get_file(file):
    if file == 'style.css' or file == 'index.js':
        print(file)
        return send_from_directory('.', file)
    else:
        return '', 200

@app.route("/keys", methods=['POST'])
def keys():
    keys = request.json['keys']
    print(keys)
    k = Controller()
    k.type(keys)
    return "OK"

import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get_ip()
port = 7474

with open('template.html') as r, open('index.html', 'w') as w:
    for l in r.readlines():
        l = l.replace('$$IP$$', str(ip))
        l = l.replace('$$PORT$$', str(port))
        w.write(l)

if __name__ == '__main__':
    print('\033[32;1m * Connect to http://{}:{}/\033[0m'.format(ip, port))
    if sys.platform.startswith('linux'):
        os.system('sudo iptables -I INPUT -p tcp --dport {} -j ACCEPT'.format(port))
    app.run(host='0.0.0.0', port=port)