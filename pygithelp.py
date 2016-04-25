#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Shai Wilson

GITHUB_API = 'https://api.github.com'

import requests
import json
import getpass

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']

# ------
# 200
# 'application/json'

# my toke "token": "856b13bbc7a553eb1520bd0787c6f52883736a57",

def main():
    
    username = raw_input('Github username: ')
    password = getpass.getpass('Github password: ')
    note = raw_input('Note (optional): ')
    
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}

    if note:
        payload['note'] = note

    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )


    # Parse Response
    j = json.loads(res.text)
    token = j['token']
    print 'New token: %s' % token


if __name__ == '__main__':
    main()