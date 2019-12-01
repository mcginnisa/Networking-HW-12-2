#!/usr/bin/env python3

from bottle import route, run, static_file

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public/')

#run(host='localhost', port=8080, debug=True)
run(host='192.168.1.105', port=8080, debug=True)
