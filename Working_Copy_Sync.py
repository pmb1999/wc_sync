# coding: utf-8

import ui
import editor
import os.path
import console
import webbrowser as wb
import clipboard as cb

#cb.set(editor.get_text())

def update_wc(sender):
    info = os.path.split(editor.get_path())
    path = info[0].split('/')[-1]
    file_name = info[1]
    cb.set(editor.get_text())
    #print 'file name - ', file_name
    url = 'working-copy://x-callback-url/write/?repo=' + path + '&path=' + file_name + '&x-success=pythonista://'
    wb.open(url)

@ui.in_background    
def commit(sender):
    info = os.path.split(editor.get_path())
    path = info[0].split('/')[-1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    encoded_m = message.replace(' ', '%20')
    url = 'working-copy://x-callback-url/commit/?repo=' + path + '&message=' + encoded_m + '&x-success=pythonista://'
    wb.open(url)
    
@ui.in_background    
def commitOne(sender):
    info = os.path.split(editor.get_path())
    file_name = info[1]
    path = info[0].split('/')[-1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    encoded_m = message.replace(' ', '%20')
    url = 'working-copy://x-callback-url/commit/?repo=' + path + '&path=' + file_name + '&message=' + encoded_m + '&x-success=pythonista://'
    wb.open(url)

view = ui.load_view('Working_Copy_Sync')

repoList = view['repoList']
copyb = view['copyb']
writeb = view['writeb']
commitOneb = view['commitOneb']
commitb = view['commitb']
pushb = view['pushb']
pullb = view['pullb']
addCurrentb = view['addCurrentb']

view.present('sidebar')