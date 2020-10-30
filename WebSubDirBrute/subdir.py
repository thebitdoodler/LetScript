#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 02:42:24 2020

@author: fr3qu3n533
"""


import requests
import socket
import sys
user_input_url = sys.argv[1]
wordlist = sys.argv[2]
extension = sys.argv[3]

def write(word):
    f1=open("write1.txt","a")
    f1.write(word+"\n")
    
fo = open(wordlist,"r+")
for i in range(2000):
    word = fo.readline(10).strip()
    surl = user_input_url+word+extension
    response = requests.get(surl)
    if (response.status_code == 200):
        print ("[+] found :- ",surl)
    write(word)
    else:
        print ("[-] Not found :- ",surl)
        pass
