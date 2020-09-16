#! /usr/bin/env python3
# coding utf-8

import requests

#alph = '0123456789abcdefghijklmnopqrstuvwxyz'

alph = '0123456789abcdef'
base = len(alph)

lenc = 0
counter = 0 

while True:
#counter -> 16
# 1000 -> [3, 14, 8] -> 3e8
	c = counter
	password = ''

	while c > 0:
		rest = c % base
		c = counter // base
		password = alph[rest] + password
	
	while len(password) < lenc:
		password = alph[0] + password

	print(counter, password)
	response = requests.post('http://127.0.0.1:5000/auth',
			json={'login': 'admin', 'password': password})

	if response.status_code == 200:
		print('SUCCESS', password)
		break

	if password == 'z'*lenc:
		lenc+=1
		counter=0
	else:
		counter+=1
	
	
