# -*- coding: utf-8 -*-
import requests
import base64

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login(license_key):
	r=requests.post(base64.b64decode('aHR0cHM6Ly92aXAuZGJ6ZGIucHcv'),data={'license':license_key})
	return 'Welcome ' in r.content
	
if __name__ == "__main__":
	license=raw_input('your license key: ')
	if len(license)<>32:
		print 'invalid license, you can buy one here https://forum.dbzdb.pw/store/category/1-vip-forum-time/'
		exit(1)
	if login(license):
		print 'you can now use the bot :)'
	else:
		print 'invalid license, you can buy one here https://forum.dbzdb.pw/store/category/1-vip-forum-time/'