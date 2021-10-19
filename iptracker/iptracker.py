#!/usr/bin/python

#Name          : trackout
#Writer(s)     : Shamanth S Samadeshi
#Description   : TrackOut is a simple IP Tracker written in Python using API from https://ipdata.com

import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print"""
  _______             _     ____        _   
 |__   __|           | |   / __ \      | |  
    | |_ __ __ _  ___| | _| |  | |_   _| |_ 
    | | '__/ _` |/ __| |/ / |  | | | | | __|
    | | | | (_| | (__|   <| |__| | |_| | |_ 
    |_|_|  \__,_|\___|_|\_\\____/ \__,_|\__|
 Python IP Tracker - Dev - Shamanth S Samadeshi
"""
print "\r"
while True:
		ip = raw_input("What Your Target IP : ")
		url = "https://api.ipdata.co/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break
