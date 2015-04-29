#!/usr/bin/python

import sys
import editor
import os
import errno
import base64
import json
import webbrowser as wb
import keychain

INSTALL_PATH = 'wc_sync'

def item_selected(sender):
	tv.close()
	key = keychain.get_password('wcSync','xcallback')
	item = sender.items[sender.selected_row]
	path = item['path']
	url = 'working-copy://x-callback-url/read/?'
	success = 'pythonista://'+INSTALL_PATH+'/rxFile.py?action=run&argv=' + os.path.join(repo,path) +'&argv='
	f = {'repo':repo,'path':path,'key':key, 'base64':'1'}
	url += urllib.urlencode(f).replace('+','%20')
	url += '&x-success=' + urllib.quote_plus(success)
	wb.open(url)


path = sys.argv[1] #The path sent through with the x-callback-url.
jsonList = sys.argv[2] # 

fileList = json.loads(jsonList)

#put filelist in sheet view
tv = ui.TableView()
#Populate ds
files = []
repo = fileList[0]['name']
for f in fileList:
	if f['kind'] != 'directory':
		files.append({'title':f['name'], 'path':f['path'], 'accessory_type': 'none', 'image':None, 'function':item_selected})
ds = ui.ListDataSource(files)			
ds.action = item_selected
tv.data_source = ds
tv.delegate = ds
tv.name = 'Select File to Pull'
#Show as sheet
tv.present(style='sheet')


				