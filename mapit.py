#! python3

import webbrowser,sys,pyperclip

params = sys.argv

if len(params) > 1:
    address = ' '.join(params[1:])
else:
    address = pyperclip.paste()

MAPS_URL = 'https://www.google.com/maps/place/'
webbrowser.open(MAPS_URL+address)
