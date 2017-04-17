#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains the WSGI configuration required to serve up your
# web application at http://divyabiyani.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

JSONcontent = ''
with open('/home/divyabiyani/Countries-Flag-API/Countries.json','r') as f:
    JSONcontent = JSONcontent + (f.readline())

Countries = '''<html>
<head>
    <title>Countries Flag</title>
</head>
<body>
<pre>''' + JSONcontent + '''
</pre>
</body>
</html>'''


def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = Countries
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Access-Control-Allow-Origin', '*')]
    start_response(status, response_headers)
    yield JSONcontent
