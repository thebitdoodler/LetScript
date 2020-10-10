#!/usr/bin/env python

import requests

def response(URL):
	try:
		return requests.get("https://" + URL)
  
	except requests.exceptions.ConnectionError:
		pass
	except requests.exceptions.InvalidURL:
		pass
target_URL = "google.com"

with open("/root/Downloads/subdomains.list","r") as wordlist:
	for line in wordlist:
		word = line.strip()
		test_URL = word + "." + target_URL
		res = response(test_URL)
		if res:
			print("[+] Discovered a new subdomain -->" + test_URL)
