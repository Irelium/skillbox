#! /usr/bin/env python3
# coding utf-8

'''	Домашнее задание №1:
- Сделать list из списка URL адресов (минимум 5).
- Написать цикл, который пробежит по списку URL и обратится к каждому N раз (минимум 100) с помощью библиотеки requests.
			Выполнил Романов Кирилл'''

import requests
import random

try:
	url = ['https://ya.ru', 'https://habr.com/ru', 'http://red-torch.ru', 'http://new.ngmu.ru/', 'https://vk.com', 'https://www.usa.gov']
	f = open('dz1.log', 'w') #открываем файл для записи ответов от сайтов.
	N = random.randint(101, 200) #не менее 100 запросов на каждый URL
	for i in url:
		for j in range(0, N):
			response = requests.get(i) #отправляем запрос на URL
			print(j, 'Sourse - ', i, 'got answer:', response)
			if j == 0: #избавляемя от избыточности - достаточно вывода одного запроса из нескольких однотипных
				print('start colleting data')
				data = response.text
				for index in data:
					f.write(str(index))
				print('data collected')
	f.close()
except KeyboardInterrupt:
	exit(1)	